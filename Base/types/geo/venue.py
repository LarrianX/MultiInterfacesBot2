from abc import ABC

from .geo_point import GeoPoint
from ..entity import Attachment


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
