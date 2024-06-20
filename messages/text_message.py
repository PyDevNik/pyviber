from message import Message
from ..message_type import MessageType
from typing import Optional

class TextMessage(Message):
    def __init__(self, text: str, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.TEXT, tracking_data=tracking_data)
        self.text = text