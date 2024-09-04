import asyncio
import os
from typing import Optional, override

import telethon.types
from telethon import TelegramClient
from telethon.events import NewMessage

from Base import BaseInterface, InputAttachment
from .interface import TelegramInterfaceStub
from .types import *
from .types.geo.geo_point import TelegramGeoPoint
from .types.geo.venue import TelegramVenue
from .types.poll.poll import TelegramPoll

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

PLATFORM = "Telegram"


class TelegramInterface(TelegramInterfaceStub):
    def __init__(self,
                 base_interface: BaseInterface,
                 api_id: int = API_ID,
                 api_hash: str = API_HASH,
                 bot_token: str = BOT_TOKEN,
                 session_name: str = "main"):
        super().__init__(base_interface)
        self.client = TelegramClient(
            session_name,
            api_id,
            api_hash,
        ).start(bot_token=bot_token)
        self.base_interface = base_interface
        self.client.add_event_handler(self._handle_message, NewMessage())

    async def _handle_message(self, event: NewMessage.Event):
        message = await TelegramMessage.from_tl(event.message, caller=self)
        await self.base_interface.message_handler(message)

    @override
    async def transform(self, tl: telethon.types.TLObject) -> TelegramEntity:
        kwargs = {"tl": tl, "caller": self}

        if isinstance(tl, (telethon.types.PeerChat, telethon.types.ChatFull)):
            return await TelegramChat.from_tl(**kwargs)

        elif isinstance(tl, telethon.types.Message):
            return await TelegramMessage.from_tl(**kwargs)

        elif isinstance(tl, (telethon.types.PeerUser, telethon.types.User)):
            return await TelegramUser.from_tl(**kwargs)

        elif isinstance(tl, telethon.types.MessageMediaDocument):
            return await TelegramDocument.from_tl(**kwargs)

        elif isinstance(tl, telethon.types.MessageMediaPhoto):
            return await TelegramPhoto.from_tl(**kwargs)

        elif isinstance(tl, telethon.types.MessageMediaGeo):
            return await TelegramGeoPoint.from_tl(**kwargs)

        elif isinstance(tl, telethon.types.MessageMediaVenue):
            return await TelegramVenue.from_tl(**kwargs)

        elif isinstance(tl, telethon.types.MessageMediaPoll):
            return await TelegramPoll.from_tl(**kwargs)

        else:
            return TelegramUnknown(source=tl, caller=self)


    @override
    async def get_entity(self, n: int | TelegramMessage) -> Optional[telethon.types.TLObject]:
        tl_object = None
        if isinstance(n, int):
            tl_object = await self.client.get_entity(n)
        elif isinstance(n, TelegramMessage):
            tl_object = await self.client.get_messages(n.from_user.id, ids=n.id)

        if tl_object:
            return tl_object


    @override
    async def send_message(self, id: int, text: str, attachments: Optional[list[InputAttachment]] = None) -> TelegramEntity:
        tl_object = await self.client.send_message(id, text)
        return await self.transform(tl_object)


    # @override
    # def start(self, loop: asyncio.AbstractEventLoop):
    #     with self.client.loop:
    #         loop.run_until_complete(self._start())

    @override
    def start(self, loop: asyncio.AbstractEventLoop):
        print("Клиент Telegram запущен.")
        self.client.loop.run_until_complete(self.send_message(1667209703, "Бот запущен."))
        self.client.loop.run_until_complete(self.client.run_until_disconnected())
