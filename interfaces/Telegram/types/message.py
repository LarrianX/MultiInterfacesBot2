from typing import Optional, override

from telethon.tl.patched import Message

from Base import ChatType, Attachment
from Base import Message as BaseMessage
from .chat import TelegramChat
from .entity import TelegramEntity, TelegramAttachment
from .user import TelegramUser
from ..interface import TelegramInterfaceStub


class TelegramMessage(TelegramEntity, BaseMessage):
    from_user: TelegramUser
    chat: TelegramChat
    attachments: list[TelegramAttachment]
    source: Optional[Message]

    @classmethod
    async def from_tl(cls, tl: Message, caller: TelegramInterfaceStub):
        attachments = []
        if tl.media:
            attachments.append(await caller.transform(tl.media))

        # if isinstance(tl.peer_id, PeerChat):
        #     user = await TelegramUser.from_tl(tl.from_id, caller=caller)
        #     chat = await TelegramChat.from_tl(tl.peer_id, caller=caller)
        # else:
        user = await TelegramUser.from_tl(tl.peer_id, caller=caller)
        chat = TelegramChat(
            id=tl.peer_id.user_id,
            type=ChatType.PRIVATE,
            title=user.first_name,
            members=[user],
            source=tl,
            caller=caller,
        )
        return cls(
            id=tl.id,
            from_user=user,
            chat=chat,
            date=tl.date,
            content=tl.message,
            attachments=attachments,
            source=tl,
            caller=caller
        )

    @override
    async def reply(self, text: str, attachments: Optional[list[Attachment]] = None):
        if not self.source and self.caller:
            self.source = await self.caller.get_entity(self.id)
            await self.reply(text, attachments)
        elif isinstance(self.source, Message):
            await self.source.reply(text)

    @override
    async def answer(self, text: str, attachments: list[Attachment] = None):
        if not self.source and self.caller:
            self.source = await self.caller.get_entity(self.id)
            await self.answer(text, attachments)
        elif isinstance(self.source, Message):
            await self.source.respond(text)

    @override
    async def edit(self, text: str, attachments: list[Attachment] = None):
        if not self.source and self.caller:
            self.source = self.caller.get_entity(self.id)
            await self.reply(text, attachments)
        elif isinstance(self.source, Message):
            await self.source.edit(text)
