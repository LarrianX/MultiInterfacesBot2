from typing import Optional
from abc import ABC, abstractmethod
from datetime import datetime
import unittest

from .entity import Entity, Attachment
from ..TestCase import TestCase
from .user import User
from .chat import Chat
from .enums import ChatType


class Message(Entity, ABC):
    """
    Обычное сообщение
    :param id: ID объекта
    :param from_user: Кто прислал сообщение
    :param chat: Чат этого сообщения
    :param date: Дата отправки
    :param content: Текст сообщения
    :param attachments: Вложения
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    from_user: User
    chat: Chat
    date: datetime
    content: str
    attachments: list[Attachment]

    @abstractmethod
    async def reply(self, text: str, attachments: list[Attachment] = None):
        pass

    @abstractmethod
    async def answer(self, text: str, attachments: list[Attachment] = None):
        pass

    @abstractmethod
    async def edit(self, text: str, attachments: list[Attachment] = None):
        pass


# class TestMessage(TestCase):
#     def test_message_initialization(self):
#         id = 1
#         from_user = User(id=1, platform="CLI", first_name="john", last_name="doe", username="john_doe", is_bot=False, source=None, caller=None)
#         chat = Chat(id=1, platform="CLI", type=ChatType.PRIVATE, title="Test Chat", members=[from_user], source=None, caller=None)
#         date = datetime.now()
#         content = "Hello, World!"
#         attachments = []
#         source = None
#         caller = None
#         chat = self._test_initialization(Message, locals())
