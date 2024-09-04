import json
import logging
import os
from datetime import datetime

from .types import *


def convert_bytes_to_str(obj):
    if isinstance(obj, dict):
        return {convert_bytes_to_str(k): convert_bytes_to_str(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_bytes_to_str(elem) for elem in obj]
    elif isinstance(obj, bytes):
        return "bytes"
    elif isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return obj


def dump(message: Message):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Добавляем новый словарь к существующим данным
    data["message"] = convert_bytes_to_str(message.source.media.to_dict())

    # Открываем файл для записи и сохраняем обновленные данные
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


class BaseInterface:
    def __init__(self):
        self.wait_download_users = []

    async def message_handler(self, message: Message):
        try:
            print(f"{message.from_user.first_name}: {message.content!r}")
            print(message)

            if message.attachments:
                print(message.attachments[0])
                print(message.attachments[0].source)

            if message.attachments and message.from_user.username in self.wait_download_users:
                message.content = "/download"
                self.wait_download_users.remove(message.from_user.username)

            # if message.source.media:
            #     dump(message)

            if message.content.startswith("/"):
                await self.command_handler(message)
        except Exception as e:
            logging.error(f"Ошибка при обработке сообщения: {type(e)} {e}")
            await message.answer("Произошла ошибка при обработке вашего сообщения.")

    async def command_handler(self, message: Message):
        try:
            raw = message.content[1:].split(" ")
            command = raw[0]
            args = raw[1:]
            func = getattr(self, command, None)
            if func:
                result = await func(message, *args)
                if result:
                    await message.reply(result)
            else:
                logging.warning(f"Неизвестная команда: {command}")
                await message.answer(f"Неизвестная команда: {command}")
        except Exception as e:
            logging.error(f"Ошибка при обработке команды: {e}")
            await message.answer("Произошла ошибка при обработке вашей команды.")

    async def _download(self, attachment: Media):
        if hasattr(attachment, "get"):
            b = await attachment.get()
            file_name = attachment.file_name
            with open(file_name, "wb") as f:
                f.write(b)
            return True
        else:
            return False

    async def echo(self, message: Message, *args):
        return message.content

    async def system(self, message: Message, *args):
        return f"Exit code: {str(os.system(" ".join(args)))}"

    async def exec(self, message: Message, *args):
        code = " ".join(args)
        local_vars = locals()
        try:
            exec(f"""async def __exec():\n\t{code}""", local_vars)
            await local_vars["__exec"]()
            return "Код выполнен успешно."
        except Exception as e:
            logging.error(f"Ошибка при выполнении кода: {e}")
            return f"Ошибка при выполнении кода: {e}"

    async def download(self, message: Message, *args):
        if message.attachments:
            success = False
            for media in message.attachments:
                if isinstance(media, Media):
                    success = await self._download(media)
            if success:
                return "Скачано!"
            else:
                return "Не скачано..."
        else:
            self.wait_download_users.append(message.from_user.username)
            return "Жду медиа..."
