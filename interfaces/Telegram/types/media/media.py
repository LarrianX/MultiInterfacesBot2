from typing import Optional

from Base import Media as BaseMedia
from ..entity import TelegramAttachment

from telethon.types import TLObject


class TelegramMedia(TelegramAttachment, BaseMedia):
    async def get(self) -> Optional[bytes]:
        if not self.source and self.caller and self.id:
            self.source = await self.caller.get_entity(self.id)
            return await self.get()

        elif isinstance(self.source, TLObject) and self.caller:
            return await self.caller.client.download_media(self.source, file=bytes)

        elif isinstance(self.source, bytes):
            return self.source
