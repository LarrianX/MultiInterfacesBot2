from abc import ABC

from .sticker import Sticker


class AnimatedSticker(Sticker, ABC):
    """
    Анимированный стикер.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param duration: Длина анимации
    :param alt: Смайл, сходный с содержанием со стикером
    :param sticker_set: Набор стикеров данного стикера
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    duration: int | float
