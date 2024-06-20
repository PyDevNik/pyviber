from message import Message
from ..message_type import MessageType
from ..keyboard import Keyboard
from typing import Optional

class UrlMessage(Message):
    def __init__(self, media: str, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.URL, keyboard=keyboard, tracking_data=tracking_data)
        self.media = media