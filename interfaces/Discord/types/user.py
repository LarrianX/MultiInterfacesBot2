from typing import Optional

from discord import User

from Base import User as BaseUser
from .entity import DiscordEntity
from ..interface import DiscordInterfaceStub


class DiscordUser(DiscordEntity, BaseUser):
    source: Optional[User] = None

    @classmethod
    async def from_ds(cls, ds: User,
                      caller: DiscordInterfaceStub):
        return cls(
            id=ds.id,
            first_name=ds.global_name,
            last_name=None,
            username=ds.name,
            is_bot=ds.bot,
            source=ds,
            caller=caller
        )
