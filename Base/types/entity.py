from typing import Optional, Any
from abc import ABC, abstractmethod

from dataclasses import dataclass
from pydantic import BaseModel

IGNORE_VARS = [
    "source",
    "caller",
    "platform"
]


class Entity(BaseModel, ABC):
    """
    Базовый класс для всех сущностей.
    :param id: ID объекта
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    id: int
    source: Optional[object] = None
    caller: Optional[object] = None

    def _get_dataclass(self):
        init_vars = vars(self).copy()
        # Убираем нежеланные значения
        for i in IGNORE_VARS:
            init_vars.pop(i)
        # Выставляем аннотации типов для каждой нашей переменной, ведь dataclass работает на них
        annotations = {}
        for var in init_vars:
            if not var.startswith("_"):
                annotations[var] = init_vars[var].__class__
        # Генерируем dataclass нашу копию
        class_ = dataclass(
            type(self.__class__.__name__, (), {"__annotations__": annotations})  # type: ignore
        )
        # Определяем в нём наши переменные и вызываем __str__
        return class_(**init_vars)

    def __str__(self):
        return self._get_dataclass().__str__()

    def __repr__(self):
        return self._get_dataclass().__repr__()

    def __xor__(self, other):
        if isinstance(other, self.__class__):
            diff = {}
            dict1 = vars(self).copy()
            dict2 = vars(other).copy()

            for i in IGNORE_VARS:
                dict1.pop(i)
                dict2.pop(i)

            for key in dict1 | dict2:
                key1 = dict1.get(key)
                key2 = dict2.get(key)
                if key1 != key2:
                    diff[key] = (key1, key2)

            return diff
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self ^ other) == {}
        else:
            return NotImplemented


class Attachment(Entity, ABC):
    """
    Базовый класс для всех типов вложений.
    """
    pass


# class SupportedAttachment(Attachment, ABC):
#     """
#     Класс для поддерживаемых вложений
#     """


class Unsupported(Attachment, ABC):
    """
    Класс для вложений, которые не поддерживаются в данный момент.
    Есть ряд функций которые реализовываться не будут из-за их специфичности
    """
    @abstractmethod
    def convert(self) -> str:
        """
        Конвертирует неподдерживаемое вложение в текст
        """
