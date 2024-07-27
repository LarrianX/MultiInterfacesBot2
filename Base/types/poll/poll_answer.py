from typing import Optional
from abc import ABC, abstractmethod
from datetime import datetime
import unittest

from ..entity import Entity
from ..user import User
from ...TestCase import TestCase


class PollAnswer(Entity, ABC):
    """
    Вариант ответа на опрос.
    :param id: ID объекта
    :param text: Текст параметра
    :param voters: Участники, которые выбрали этот вариант
    :param correct: Если опрос в режиме викторины, правильный ли данный ответ, иначе None
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    text: str
    voters: list[User]
    correct: Optional[bool]


class TestPollAnswer(TestCase):
    def test_poll_answer_initialization(self):
        id = 1
        text = "Option 1"
        voters = [User(id=1, platform="CLI", first_name="john", last_name="doe", username="john_doe", is_bot=False, source=None, caller=None)]
        correct = None
        source = None
        caller = None
        poll_answer = self._test_initialization(PollAnswer, locals())
