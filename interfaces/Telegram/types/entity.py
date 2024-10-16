from abc import ABC
from typing import Optional

from pydantic import ConfigDict
from telethon.tl.types import TLObject

from Base import Entity, Attachment, Unsupported
from ..TestCase import TestCase
from ..constants import *
from ..interface import TelegramInterfaceStub


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
