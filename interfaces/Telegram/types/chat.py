from typing import Optional

from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types.messages import ChatFull
from telethon.types import PeerChat, Message

from Base import Chat as BaseChat
from Base import ChatType
from .entity import TelegramEntity
from .user import TelegramUser
from ..TestCase import TestCase
from ..interface import TelegramInterfaceStub


class TelegramChat(TelegramEntity, BaseChat):
    source: Optional[ChatFull | Message] = None
    members: list[TelegramUser]

    @classmethod
    async def from_tl(cls, tl: PeerChat | ChatFull, caller: TelegramInterfaceStub):
        """
        Пометка: только для групп!
        Пометка 2: не для супергрупп!
        """
        if isinstance(tl, PeerChat):
            tl: ChatFull = await caller.client(GetFullChatRequest(tl.chat_id))

        return cls(
            id=tl.full_chat.id,
            type=ChatType.GROUP,
            title=tl.chats[0].title,
            members=[await TelegramUser.from_tl(user, caller=caller) for user in
                     tl.full_chat.participants.participants],
            #       await TelegramChatParticipant.from_tl(user, rights=tl.chats[0].default_banned_rights, caller=caller)
            #       for user in tl.full_chat.participants.participants],
            source=tl,
            caller=caller
        )


class TestTelegramChat(TestCase):
    def test_telegram_chat_initialization(self):
        with self.client:
            chat = self.client.loop.run_until_complete(TelegramChat.from_tl(PeerChat(chat_id=4203535708), self))
        benchmark = TelegramChat(id=4203535708, type=ChatType.GROUP, title='default group', members=[
            TelegramUser(id=5961469393, first_name='Polaroid', last_name=None, username='poldaroidbot', is_bot=True),
            TelegramUser(id=6306597115, first_name='nothing', last_name=None, username='shaurmaJ', is_bot=False),
            TelegramUser(id=1667209703, first_name='онигири', last_name=None, username='Y_kto_to', is_bot=False)
        ])
        self.assertEqual(chat, benchmark)
