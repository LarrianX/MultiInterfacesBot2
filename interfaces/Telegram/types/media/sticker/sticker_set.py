from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types.messages import StickerSet
from telethon.types import InputStickerSetID

from Base import StickerSet as BaseStickerSet
from ...entity import TelegramEntity
from ....interface import TelegramInterfaceStub


class TelegramStickerSet(TelegramEntity, BaseStickerSet):
    @classmethod
    async def from_tl(cls, tl: InputStickerSetID, caller: TelegramInterfaceStub):
        sticker_set: StickerSet = await caller.client(GetStickerSetRequest(tl, 0))
        return cls(
            id=sticker_set.set.id,
            title=sticker_set.set.title,
            count_stickers=sticker_set.set.count,
            source=sticker_set,
            caller=caller
        )
