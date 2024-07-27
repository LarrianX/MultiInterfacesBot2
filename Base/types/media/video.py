from typing import Optional
from abc import ABC, abstractmethod
import unittest

from Base.types.media import Media
from Base.TestCase import TestCase


class Video(Media, ABC):
    """
    Видео.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param duration: Длина видео
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    duration: int | float


class TestVideo(TestCase):
    def test_video_initialization(self):
        id = 1
        file_name = "example.mp4"
        file_size = 1024
        duration = 3.6
        source = None
        caller = None
        video = self._test_initialization(Video, locals())
