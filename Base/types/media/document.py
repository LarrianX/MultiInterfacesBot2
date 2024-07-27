from typing import Optional
from abc import ABC, abstractmethod
import unittest

from .media import Media
from ...TestCase import TestCase


class Document(Media, ABC):
    """
    Фотография.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """


class TestDocument(TestCase):
    def test_document_initialization(self):
        id = 1
        file_name = "example.mp4"
        file_size = 1024
        source = None
        caller = None
        document = self._test_initialization(Document, locals())
