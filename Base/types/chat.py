from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .entity import Entity
from .enums import ChatType
from .user import User
from ..TestCase import TestCase


class Chat(Entity, ABC):
    """
    Чат или группа.
    :param id: ID объекта
    :param platform: Платформа на которой расположен чат. Пример: Telegram
    :param type: Тип чата
    :param title: Название чата
    :param members: Участники чата
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    platform: str
    type: ChatType
    title: str
    members: list[User]


class TestChat(TestCase):
    def test_chat_initialization(self):
        id = 1
        platform = "CLI"
        type = ChatType.PRIVATE
        title = "Test Chat"
        members = [User(id=1, platform="CLI", first_name="john", last_name="doe", username="john_doe", is_bot=False, source=None, caller=None)]
        source = None
        caller = None
        chat = self._test_initialization(Chat, locals())
