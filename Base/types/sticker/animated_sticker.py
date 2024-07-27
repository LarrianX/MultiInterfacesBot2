from abc import ABC

from .sticker import Sticker
from ...TestCase import TestCase


class AnimatedSticker(Sticker, ABC):
    """
    Анимированный стикер.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param duration: Длина анимации
    :param alt: Смайл, сходный с содержанием со стикером
    :param sticker_set: Набор стикеров данного стикера
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    duration: int | float


class TestAnimatedSticker(TestCase):
    def test_animated_sticker_initialization(self):
        id = 1
        file_name = "sticker.mp4"
        file_size = 1024
        duration = 3.6
        alt = "⭐"
        sticker_set = None
        source = None
        caller = None
        animated_sticker = self._test_initialization(AnimatedSticker, locals())
