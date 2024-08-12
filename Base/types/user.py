from typing import Optional
from abc import ABC

from .entity import Entity


class User(Entity, ABC):
    """
    Пользователь.
    :param id: ID объекта
    :param first_name: Имя
    :param last_name: Фамилия
    :param username: Никнейм
    :param is_bot: Является ли ботом
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    is_bot: bool
