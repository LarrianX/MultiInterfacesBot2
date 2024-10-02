import asyncio
import importlib
import json
import os
from typing import Type
from dotenv import load_dotenv
from threading import Thread

from Base import BaseInterface, Interface

from interfaces.Discord import DiscordInterface
from interfaces.Telegram import TelegramInterface

load_dotenv()

DIRECTORY = "interfaces"


def load_interfaces(base_interface: BaseInterface, directory=DIRECTORY, list="list.json"):
    results = []

    # Проходим по всем папкам в указанной директории
    if list in os.listdir(directory):
        list_of_interfaces = json.load(open(os.path.join(os.getcwd(), directory, list)))

        for i in list_of_interfaces:
            module_name = f"{directory}.{i}"
            # try:
            # Импортируем модуль
            module = importlib.import_module(module_name)

            # Проверяем наличие подкласса BaseInterface
            if hasattr(module, "get"):
                interface: Type = module.get()
                if issubclass(interface, Interface):
                    obj = interface(base_interface)
                    results.append(obj)
            # except ImportError as e:
            #     print(f"Ошибка при импорте модуля: {module_name}: {repr(e)}")

    return results


if __name__ == '__main__':
    # Запуск ядра
    base = BaseInterface()
    # print(interfaces)
    discord = Thread(target=lambda: DiscordInterface(base).start(asyncio.new_event_loop()))
    discord.start()
    TelegramInterface(base).start(None)
