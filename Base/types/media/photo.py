from abc import ABC

from .media import Media


class Photo(Media, ABC):
    """
    Фотография.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
