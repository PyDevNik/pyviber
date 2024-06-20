from abc import ABC
from ..message_type import MessageType
from ..keyboard import Keyboard
from typing import Optional

class Message(ABC):
    def __init__(self, type: MessageType, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        self.type = type
        self.tracking_data = tracking_data
