import os
from abc import ABC
from typing import Optional

from dotenv import load_dotenv
from pydantic import ConfigDict
from telethon.tl.types import TLObject

from Base import Entity, Attachment, Unsupported
from ..TestCase import TestCase
from ..constants import *
from ..interface import TelegramInterfaceStub

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


class TelegramEntity(Entity):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    platform: str = PLATFORM
    source: Optional[TLObject] = None
    caller: Optional[TelegramInterfaceStub | TestCase] = None


class TelegramAttachment(TelegramEntity, Attachment):
    pass


class TelegramUnsupported(TelegramAttachment, Unsupported, ABC):
    pass


class TelegramUnknown(TelegramUnsupported):
    id: None = None

    async def convert(self) -> str:
        return "Unknown type"
