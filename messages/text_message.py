from message import Message
from ..message_type import MessageType
from ..keyboard import Keyboard
from typing import Optional

class TextMessage(Message):
    def __init__(self, text: str, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.TEXT, keyboard=keyboard, tracking_data=tracking_data)
        self.text = text