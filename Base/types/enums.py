from typing import Optional, Any
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


from enum import Enum


class ChatType(Enum):
    """
    Типы чатов.
    """
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"
    