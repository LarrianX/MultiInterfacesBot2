from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .media import Media
from ...TestCase import TestCase


class Photo(Media, ABC):
    """
    Фотография.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """


class TestPhoto(TestCase):
    def test_photo_initialization(self):
        id = 1
        file_name = "example.mp4"
        file_size = 1024
        source = None
        caller = None
        photo = self._test_initialization(Photo, locals())
