from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .media import Media
from ...TestCase import TestCase


class Audio(Media, ABC):
    """
    Аудио или голосовые сообщения.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param duration: Длина аудио
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    duration: int | float


class TestAudio(TestCase):
    def test_audio_initialization(self):
        id = 1
        file_name = "example.mp4"
        file_size = 1024
        duration = 3.6
        source = None
        caller = None
        audio = self._test_initialization(Audio, locals())
