from typing import Optional
from abc import ABC, abstractmethod
import unittest

from Base.types.entity import Attachment
from Base.TestCase import TestCase


class GeoPoint(Attachment, ABC):
    """
    Геопозиция.
    :param id: ID объекта
    :param latitude: Широта
    :param longitude: Долгота
    :param accuracy: Точность в метрах
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    latitude: float
    longitude: float
    accuracy: Optional[float] = None


class TestGeoPoint(TestCase):
    def test_geo_point_initialization(self):
        id = 1
        latitude = 56.0
        longitude = 37.0
        accuracy = 10.0
        source = None
        caller = None
        geo_point = self._test_initialization(GeoPoint, locals())
