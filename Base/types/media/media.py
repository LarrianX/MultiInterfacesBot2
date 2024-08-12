from abc import ABC, abstractmethod

from ..entity import Attachment


class Media(Attachment, ABC):
    """
    Базовый класс для всех медиа.
    :param id: ID объекта
    :param file_name: Имя файла
    :param file_size: Размер файла
    :param source: Если преобразовано из другого типа данных, то указывается он
    :param caller: Интерфейс, создавший этот объект
    """
    file_name: str
    file_size: int

    @abstractmethod
    async def get(self):
        pass
