import asyncio
from abc import ABC, abstractmethod
from typing import Optional

from .types import *
from .main import BaseInterface


class Interface(ABC):
    def __init__(self, base_interface: BaseInterface):
        self.base_interface = base_interface

    @abstractmethod
    async def get_entity(self, id: int):
        pass

    @abstractmethod
    async def send_message(self, id: int, text: str, attachments: Optional[list[InputAttachment]] = None) -> Message:
        pass

    @abstractmethod
    def start(self, loop: asyncio.AbstractEventLoop):
        pass
