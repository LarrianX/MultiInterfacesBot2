from abc import ABC, abstractmethod
from datetime import datetime

from .chat import Chat
from .entity import Entity, Attachment
from .user import User


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
