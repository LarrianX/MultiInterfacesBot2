from telethon.types import GeoPoint, MessageMediaGeo

from Base import GeoPoint as BaseGeoPoint
from ..entity import TelegramAttachment
from ...interface import TelegramInterfaceStub


class TelegramGeoPoint(TelegramAttachment, BaseGeoPoint):
    id: None = None

    @classmethod
    async def from_tl(cls, tl: GeoPoint | MessageMediaGeo, caller: TelegramInterfaceStub):
        if isinstance(tl, MessageMediaGeo):
            return await cls.from_tl(tl.geo, caller)

        return TelegramGeoPoint(
            longitude=tl.long,
            latitude=tl.lat,
            accuracy=tl.accuracy_radius,
            source=tl,
            caller=caller
        )
