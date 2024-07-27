from typing import Optional
from abc import ABC, abstractmethod
import unittest

from ..entity import Attachment
from ...TestCase import TestCase


class Media(Attachment, ABC):
    """
    Базовый класс для всех медиа.
    :param file_name: Имя файла
    :param file_size: Размер файла
    """
    file_name: str
    file_size: int


class TestMedia(TestCase):
    def test_media_initialization(self):
        id = 1
        file_name = "example.mp4"
        file_size = 1024
        source = None
        caller = None
        media = self._test_initialization(Media, locals())
