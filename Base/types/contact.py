from abc import ABC
from typing import Optional

from .entity import Attachment


class Contact(Attachment, ABC):
    """
    Контакт.
    :param id: ID объекта
    :param phone_number: Номер телефона
    :param first_name: Имя
    :param last_name: Фамилия
    :param username: Никнейм
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    phone_number: str
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
