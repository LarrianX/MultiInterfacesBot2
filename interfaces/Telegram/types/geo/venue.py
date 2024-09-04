from telethon.types import MessageMediaVenue

from Base import Venue as BaseVenue
from .geo_point import TelegramGeoPoint
from ..entity import TelegramAttachment
from ...interface import TelegramInterfaceStub


class TelegramVenue(TelegramAttachment, BaseVenue):
    geo: TelegramGeoPoint
    venue_id: str
    id: None = None

    @classmethod
    async def from_tl(cls, tl: MessageMediaVenue, caller: TelegramInterfaceStub):
        return cls(
            venue_id=tl.venue_id,
            geo=await TelegramGeoPoint.from_tl(tl.geo, caller),
            title=tl.title,
            address=tl.address,
            source=tl,
            caller=caller
        )
