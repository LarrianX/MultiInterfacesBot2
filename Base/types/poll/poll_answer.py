from abc import ABC
from typing import Optional

from ..entity import Entity
from ..user import User


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
    voters: list[User] | int
    correct: Optional[bool]
