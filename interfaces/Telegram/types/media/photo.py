from telethon.types import MessageMediaPhoto

from Base import Photo as BasePhoto
from .media import TelegramMedia
from ...interface import TelegramInterfaceStub


class TelegramPhoto(TelegramMedia, BasePhoto):
    @classmethod
    async def from_tl(cls, tl: MessageMediaPhoto, caller: TelegramInterfaceStub):
        photo = tl.photo
        size: int = max(photo.sizes[-1].sizes)
        return cls(
            id=photo.id,
            file_name="image.jpeg",
            file_size=size,
            source=tl,
            caller=caller
        )
