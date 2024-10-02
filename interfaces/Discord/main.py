import asyncio
import os
from typing import Optional

import discord
from dotenv import load_dotenv

from Base import InputAttachment, Message, BaseInterface
from .interface import DiscordInterfaceStub
from .types import *
from .types.entity import DiscordUnknown

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls._instance

class DiscordClient(discord.Client):
    async def on_ready(self):
        if not (user := self.get_user(397006943773917194)):
            user = await self.fetch_user(397006943773917194)
        await user.send("Клиент Discord запущен.")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        instance: Optional[DiscordInterface] = DiscordInterface.get_instance()
        if instance:
            await instance.base_interface.message_handler(
                await instance.transform(message)  # type: ignore
            )

class DiscordInterface(DiscordInterfaceStub, Singleton):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, base_interface: BaseInterface):
        super().__init__(base_interface)
        intents = discord.Intents.default()
        intents.message_content = True
        self.client: DiscordClient = DiscordClient(intents=intents)

    async def transform(self, ds: object) -> DiscordEntity:
        if isinstance(ds, discord.Message):
            return await DiscordMessage.from_ds(ds, caller=self)

        else:
            return DiscordUnknown(source=ds, caller=self)

    async def get_entity(self, id: int):
        pass

    async def send_message(self, id: int, text: str, attachments: Optional[list[InputAttachment]] = None) -> Message:
        pass

    def start(self, loop: asyncio.AbstractEventLoop):
        self.client.run(BOT_TOKEN)
