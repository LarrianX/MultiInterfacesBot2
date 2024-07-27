from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .entity import Entity
from ..TestCase import TestCase


class User(Entity, ABC):
    """
    Пользователь.
    :param id: ID объекта
    :param platform: Платформа на которой расположен пользователь. Пример: Discord
    :param first_name: Имя
    :param last_name: Фамилия
    :param username: Никнейм
    :param is_bot: Является ли ботом
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    platform: str
    first_name: str
    last_name: str
    username: str
    is_bot: bool


class TestUser(TestCase):
    def test_user_initialization(self):
        id = 1
        platform = "CLI"
        first_name = "John"
        last_name = "Doe"
        username = "john_doe"
        is_bot = False
        source = None
        caller = None
        user = self._test_initialization(User, locals())
