from abc import ABC

from .entity import Entity
from .enums import ChatType
from .user import User


class Chat(Entity, ABC):
    """
    Чат или группа.
    :param id: ID объекта
    :param type: Тип чата
    :param title: Название чата
    :param members: Участники чата
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    type: ChatType
    title: str
    members: list[User]
