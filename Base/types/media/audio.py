from abc import ABC

from .media import Media


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
