from typing import Optional
from abc import ABC
from datetime import datetime

from .poll_answer import PollAnswer
from ..entity import Entity
from ..user import User


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
