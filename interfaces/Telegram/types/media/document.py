from Base import Document as BaseDocument
from .media import TelegramMedia
from .audio import TelegramAudio
from .photo import TelegramPhoto
from .video import TelegramVideo
from ...interface import TelegramInterfaceStub

import telethon.types


def rstrip_untrusted(string):
    """
    Удаляет только одно вхождение символов (chars) с конца строки.
    """
    # Проверяем, что строка заканчивается на указанный символ
    if string.endswith(".untrusted"):
        index = len(string) - len(".untrusted")
        return string[:index]
    else:
        return string


class TelegramDocument(TelegramMedia, BaseDocument):
    @classmethod
    async def from_tl(cls, tl: telethon.types.MessageMediaDocument, caller: TelegramInterfaceStub):
        """
        Возвращает не только TelegramDocument.
        """
        document = tl.document
        size: int = document.size

        kwargs = {
            "id": document.id,
            "file_size": size,
            "source": tl,
            "caller": caller
        }

        # Обработка атрибутов
        sticker_attributes = audio_attributes = image_attributes = video_attributes = file_name = None
        for attr in document.attributes:
            if isinstance(attr, telethon.types.DocumentAttributeFilename):
                file_name = attr.file_name
            elif isinstance(attr, telethon.types.DocumentAttributeAudio):
                audio_attributes = attr
            elif isinstance(attr, telethon.types.DocumentAttributeImageSize):
                image_attributes = attr
            elif isinstance(attr, telethon.types.DocumentAttributeVideo):
                video_attributes = attr
            elif isinstance(attr, telethon.types.DocumentAttributeSticker):
                sticker_attributes = attr

        if video_attributes:
            # Видео
            return TelegramVideo(
                **kwargs,
                duration=video_attributes.duration,
                file_name=file_name if file_name else "video.mp4"
            )
        elif audio_attributes:
            # Аудио
            return TelegramAudio(
                **kwargs,
                duration=audio_attributes.duration,
                file_name=file_name if file_name else "audio.ogg"
            )
        else:
            # Документ
            return cls(
                **kwargs,
                file_name=rstrip_untrusted(file_name)
            )
