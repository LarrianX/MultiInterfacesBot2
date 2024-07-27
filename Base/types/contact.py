from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .entity import Attachment
from ..TestCase import TestCase


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


class TestContact(TestCase):
    def test_contact_initialization(self):
        id = 1
        phone_number = "+7 999 999-99-99"
        first_name = "John"
        last_name = "Doe"
        username = "john_doe"
        source = None
        caller = None
        media = self._test_initialization(Contact, locals())
