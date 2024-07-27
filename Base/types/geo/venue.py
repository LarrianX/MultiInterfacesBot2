from abc import ABC

from Base.types.entity import Attachment
from Base.types.geo.geo_point import GeoPoint
from Base.TestCase import TestCase


class Venue(Attachment, ABC):
    """
    Место на карте.
    :param id: ID объекта
    :param geo: Геопозиция
    :param title: Название
    :param address: Адрес
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    geo: GeoPoint
    title: str
    address: str


class TestVenue(TestCase):
    def test_venue_initialization(self):
        id = 1
        geo = GeoPoint(id=1, latitude=56.0, longitude=37.0, accuracy=10.0, source=None, caller=None)
        title = "Sight"
        address = "Street 1, 123"
        source = None
        caller = None
        venue = self._test_initialization(Venue, locals())
