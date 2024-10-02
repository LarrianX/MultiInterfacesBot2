import os
import unittest

from dotenv import load_dotenv
from telethon import TelegramClient

from .constants import SESSION_NAME

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


class TestCase(unittest.TestCase):
    # def assertEqual(self, first, second, msg=None):
    #     if isinstance(first, Entity) and isinstance(second, Entity):
    #         attributes1: dict[str, Any] = vars(first).copy()
    #         attributes2: dict[str, Any] = vars(second).copy()
    #         for var in IGNORE_VARS:
    #             attributes1.pop(var)
    #             attributes2.pop(var)
    #         return self.assertEqual(attributes1, attributes2)
    #     else:
    #         return super().assertEqual(first, second, msg)

    def setUp(self):
        self.client = TelegramClient(
            SESSION_NAME,
            API_ID,
            API_HASH,
        ).start(bot_token=BOT_TOKEN)
