import asyncio
import threading
import importlib
import os
from typing import Any
from telethon.types import Message

# from interfaces.base import Interface, BaseInterface

DIRECTORY = "interfaces"


def load_interfaces(base_interface: Any, directory=DIRECTORY):
    results = []

    # Проходим по всем папкам в указанной директории
    for root, dirs, files in os.walk(directory):
        if '__init__.py' in files and root != directory:
            # Определяем модульное имя по пути
            module_name = os.path.relpath(root, os.getcwd()).replace(os.sep, '.')

            try:
                # Импортируем модуль
                module = importlib.import_module(module_name)

                # Проверяем наличие метода get
                if hasattr(module, 'get') and callable(getattr(module, 'get')):
                    # Вызываем метод get и добавляем результат в список
                    class_ = module.get()
                    results.append(class_(base_interface))

            except Exception as e:
                print(f"Ошибка при импорте модуля {module_name}: {e}")

    return results


async def start_interfaces(interfaces: list[Any]) -> list[threading.Thread]:
    loop = asyncio.get_event_loop()
    threads = []
    for obj in interfaces:
        thread = threading.Thread(target=obj.start(), args=(loop,))
        threads.append(thread)
        thread.start()
    return threads


if __name__ == '__main__':
    # Запуск ядра
    base = BaseInterface(None)
    interfaces: list[Any] = load_interfaces(base)
    # print(interfaces)

    asyncio.run(start_interfaces(interfaces))
