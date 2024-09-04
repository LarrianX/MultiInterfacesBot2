from abc import ABC
from typing import Optional

from ..entity import Attachment


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
