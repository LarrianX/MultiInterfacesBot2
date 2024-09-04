from typing import Optional

from telethon.types import PeerUser, User, ChatParticipant, ChatParticipantCreator, ChatParticipantAdmin

from Base import User as BaseUser
from .entity import TelegramEntity
from ..TestCase import TestCase
from ..interface import TelegramInterfaceStub


class TelegramUser(TelegramEntity, BaseUser):
    source: Optional[User] = None

    @classmethod
    async def from_tl(cls, tl: PeerUser | ChatParticipant | ChatParticipantCreator | ChatParticipantAdmin | User,
                      caller: TelegramInterfaceStub):
        if isinstance(tl, (PeerUser, ChatParticipant, ChatParticipantCreator, ChatParticipantAdmin)):
            tl: User = await caller.client.get_entity(tl.user_id)

        return cls(
            id=tl.id,
            first_name=tl.first_name,
            last_name=tl.last_name,
            username=tl.username,
            is_bot=tl.bot,
            source=tl,
            caller=caller
        )


class TestTelegramUser(TestCase):
    def test_telegram_user_initialization(self):
        with self.client:
            user: TelegramUser = self.client.loop.run_until_complete(
                TelegramUser.from_tl(PeerUser(user_id=1667209703), self))
        benchmark = TelegramUser(id=1667209703, first_name='онигири', last_name=None, username='Y_kto_to', is_bot=False)
        self.assertEqual(user, benchmark)
