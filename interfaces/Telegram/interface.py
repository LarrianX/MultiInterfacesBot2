from abc import ABC, abstractmethod

from telethon import TelegramClient
from telethon.tl.types import TLObject

from Base import Interface, Entity


class TelegramInterfaceStub(Interface, ABC):
    client: TelegramClient

    @abstractmethod
    async def transform(self, tl: TLObject) -> Entity:
        pass
