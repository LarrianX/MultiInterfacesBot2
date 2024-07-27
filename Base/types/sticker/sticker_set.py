from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .. import Attachment
from ...TestCase import TestCase


class StickerSet(Attachment, ABC):
    """
    Набор стикеров.
    :param id: ID объекта
    :param title: Название набора
    :param count_stickers: Количество стикеров в наборе
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    title: str
    count_stickers: int


class TestStickerSet(TestCase):
    def test_sticker_set_initialization(self):
        id = 1
        title = "Example Sticker Set"
        count_stickers = 100
        source = None
        caller = None
        sticker_set = self._test_initialization(StickerSet, locals())
