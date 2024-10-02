from typing import Optional, override

from discord import Message

from Base import ChatType, Attachment
from Base import Message as BaseMessage
from .chat import DiscordChat
from .entity import DiscordEntity, DiscordAttachment
from .user import DiscordUser
from ..interface import DiscordInterfaceStub


class DiscordMessage(DiscordEntity, BaseMessage):
    from_user: DiscordUser
    chat: DiscordChat
    attachments: list[DiscordAttachment]
    source: Optional[Message]

    @classmethod
    async def from_ds(cls, ds: Message, caller: DiscordInterfaceStub):
        # attachments = []
        # if ds.media:
        #     attachments.append(await caller.transform(ds.media))

        user = await DiscordUser.from_ds(ds.author, caller=caller)
        chat = DiscordChat(
            id=ds.channel.id,
            type=ChatType.PRIVATE,
            title=user.username,
            members=[user],
            source=ds,
            caller=caller,
        )
        return cls(
            id=ds.id,
            from_user=user,
            chat=chat,
            date=ds.created_at,
            content=ds.content,
            attachments=[],
            source=ds,
            caller=caller
        )

    @override
    async def reply(self, text: str, attachments: Optional[list[Attachment]] = None):
        await self.source.reply(text)

    @override
    async def answer(self, text: str, attachments: Optional[list[Attachment]] = None):
        await self.source.reply(text)

    @override
    async def edit(self, text: str, attachments: Optional[list[Attachment]] = None):
        pass