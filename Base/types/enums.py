from enum import Enum


class ChatType(Enum):
    """
    Типы чатов.
    """
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"
    