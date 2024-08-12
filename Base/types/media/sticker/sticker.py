from abc import ABC

from ..media import Media


class Sticker(Media, ABC):
    """
    Стикер.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param alt: Смайл, сходный с содержанием со стикером
    :param sticker_set: Набор стикеров данного стикера
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    alt: str
    sticker_set: object
