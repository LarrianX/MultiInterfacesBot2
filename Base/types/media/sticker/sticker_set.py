from abc import ABC

from Base.types.entity import Attachment


class StickerSet(Attachment, ABC):
    """
    Набор стикеров.
    :param id: ID объекта
    :param title: Название набора
    :param count_stickers: Количество стикеров в наборе
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    title: str
    count_stickers: int
