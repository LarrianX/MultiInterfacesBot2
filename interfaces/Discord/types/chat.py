from typing import Optional, Any

from discord import Message
from discord.abc import GuildChannel

from Base import Chat as BaseChat
from Base import ChatType
from .entity import DiscordEntity
from .user import DiscordUser
from ..interface import DiscordInterfaceStub


class DiscordChat(DiscordEntity, BaseChat):
    source: Any = None
    members: list[DiscordUser]