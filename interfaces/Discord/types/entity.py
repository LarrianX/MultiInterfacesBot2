from abc import ABC
from typing import Optional

from pydantic import ConfigDict
from telethon.tl.types import TLObject

from Base import Entity, Attachment, Unsupported
from ..constants import *
from ..interface import DiscordInterfaceStub


class DiscordEntity(Entity):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    platform: str = PLATFORM
    source: Optional[TLObject] = None
    caller: Optional[DiscordInterfaceStub] = None


class DiscordAttachment(DiscordEntity, Attachment):
    pass


class DiscordUnsupported(DiscordAttachment, Unsupported, ABC):
    pass


class DiscordUnknown(DiscordUnsupported):
    id: None = None

    async def convert(self) -> str:
        return "Unknown type"
