from message import Message
from ..message_type import MessageType
from typing import Optional

class UrlMessage(Message):
    def __init__(self, media: str, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.URL, tracking_data=tracking_data)
        self.media = media