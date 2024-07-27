from typing import Optional
from abc import ABC, abstractmethod
from datetime import datetime
import unittest

from .poll_answer import PollAnswer
from ..entity import Entity
from ..user import User
from ...TestCase import TestCase


class Poll(Entity, ABC):
    """
    Опрос.
    :param id: ID объекта
    :param question: Вопрос
    :param answers: Варианты ответа
    :param voters: Проголосовавшие люди
    :param public_votes: Видно ли кто проголосовал
    :param multiple_choice: Разрешено несколько вариантов ответа
    :param quiz: Режим викторины
    :param solution: Если в режиме викторины, правильный ответ, иначе None
    :param closed: Закрыт ли опрос
    :param close_period: Время в секундах до окончания опроса
    :param close_date: Время окончания опроса
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    question: str
    answers: list[PollAnswer]
    voters: list[User]
    public_votes: bool
    multiple_choice: bool
    quiz: bool
    solution: Optional[PollAnswer]
    closed: bool
    close_period: Optional[int]
    close_date: Optional[datetime]


class TestPoll(TestCase):
    def test_poll_initialization(self):
        id = 1
        question = "What is your favorite color?"
        answers = [PollAnswer(id=1, text="Red", voters=[], correct=False, source=None, caller=None),
                   PollAnswer(id=2, text="Blue", voters=[User(id=1, platform="CLI", first_name="john", last_name="doe", username="john_doe", is_bot=False, source=None, caller=None)], correct=True, source=None, caller=None)]
        voters = [User(id=1, platform="CLI", first_name="john", last_name="doe", username="john_doe", is_bot=False, source=None, caller=None)]
        public_votes = True
        multiple_choice = False
        quiz = False
        solution = None
        closed = False
        close_period = 3600
        close_date = datetime.now()
        source = None
        caller = None
        poll = self._test_initialization(Poll, locals())
