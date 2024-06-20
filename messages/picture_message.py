from message import Message
from ..message_type import MessageType
from ..keyboard import Keyboard
from typing import Optional

class PictureMessage(Message):
    def __init__(self, text: str, media: str, thumbnail: Optional[str] = None, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.PICTURE, keyboard=keyboard, tracking_data=tracking_data)
        self.text = text
        self.media = media
        self.thumbnail = thumbnail
