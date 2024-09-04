from telethon.types import MessageMediaPoll

from Base import Poll as BasePoll
from .poll_answer import TelegramPollAnswer
from ..entity import TelegramAttachment
from ..user import TelegramUser
from ...interface import TelegramInterfaceStub


class TelegramPoll(TelegramAttachment, BasePoll):
    @classmethod
    async def from_tl(cls, tl: MessageMediaPoll, caller: TelegramInterfaceStub):
        answers = []
        for answer in tl.poll.answers:
            answers.append(TelegramPollAnswer(
                id=tl.poll.id,
                text=answer.text.text,
                voters=0,
                correct=None,
                source=tl.poll,
                caller=caller
            ))

        if tl.results.recent_voters:
            voters = []
            for user in tl.results.recent_voters:
                voters.append(await TelegramUser.from_tl(user, caller=caller))
        else:
            voters = tl.results.total_voters

        solution = tl.results.solution if tl.poll.quiz and tl.results.solution else None

        return cls(
            id=tl.poll.id,
            question=tl.poll.question.text,
            answers=answers,
            voters=voters,
            public_votes=tl.poll.public_voters,
            multiple_choice=tl.poll.multiple_choice,
            quiz=tl.poll.quiz,
            solution=solution,
            closed=tl.poll.closed,
            close_period=tl.poll.close_period,
            close_date=tl.poll.close_date,
            source=tl.poll,
            caller=caller
        )
