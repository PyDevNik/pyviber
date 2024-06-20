from message import Message
from ..message_type import MessageType
from ..keyboard import Keyboard
from typing import Optional

class FileMessage(Message):
    def __init__(self, media: str, size: int, file_name: str, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.FILE, keyboard=keyboard, tracking_data=tracking_data)
        self.media = media
        self.size = size
        self.file_name = file_name
