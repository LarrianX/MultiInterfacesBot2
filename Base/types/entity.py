from typing import Optional
from abc import ABC

from pydantic import BaseModel


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


class Attachment(Entity, ABC):
    """
    Базовый класс для всех типов вложений.
    """
    pass


class Unsupported(Attachment, ABC):
    """
    Класс для вложений, которые не поддерживаются в данный момент.
    Есть ряд функций которые реализовываться не будут из-за их специфичности
    """