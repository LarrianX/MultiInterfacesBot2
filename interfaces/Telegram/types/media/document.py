import telethon.types

from Base import Document as BaseDocument
from .audio import TelegramAudio
from .media import TelegramMedia
from .photo import TelegramPhoto
from .sticker import TelegramAnimatedSticker, TelegramSticker, TelegramStickerSet
from .video import TelegramVideo
from ...interface import TelegramInterfaceStub


def strip_untrusted(string):
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

        if sticker_attributes:
            # Стикер
            if isinstance(sticker_attributes.stickerset, telethon.types.InputStickerSetID):
                sticker_set = await TelegramStickerSet.from_tl(sticker_attributes.stickerset, caller=caller)
            else:
                sticker_set = sticker_attributes.stickerset

            if video_attributes:
                return TelegramAnimatedSticker(
                    **kwargs,
                    alt=sticker_attributes.alt,
                    sticker_set=sticker_set,
                    duration=video_attributes.duration,
                    file_name=file_name if file_name else "sticker.webm"
                )
            else:
                return TelegramSticker(
                    **kwargs,
                    alt=sticker_attributes.alt,
                    sticker_set=sticker_set,
                    file_name=file_name if file_name else "sticker.webp"
                )

        elif video_attributes:
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
        elif image_attributes:
            # Фото, скинутое в виде файла
            return TelegramPhoto(
                **kwargs,
                file_name=file_name if file_name else "photo.jpg"
            )
        else:
            # Документ
            return cls(
                **kwargs,
                file_name=strip_untrusted(file_name)
            )
