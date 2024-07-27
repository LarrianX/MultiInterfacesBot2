from typing import Optional
from abc import ABC, abstractmethod
import unittest

from ..media import Media
from ...TestCase import TestCase


class Sticker(Media, ABC):
    """
    Стикер.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param alt: Смайл, сходный с содержанием со стикером
    :param sticker_set: Набор стикеров данного стикера
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    alt: str
    sticker_set: object


class TestSticker(TestCase):
    def test_sticker_initialization(self):
        id = 1
        file_name = "sticker.webp"
        file_size = 1024
        alt = "⭐"
        sticker_set = None
        source = None
        caller = None
        sticker = self._test_initialization(Sticker, locals())
