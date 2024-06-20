from message import Message
from ..message_type import MessageType
from typing import Optional

class FileMessage(Message):
    def __init__(self, media: str, size: int, file_name: str, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.FILE, tracking_data=tracking_data)
        self.media = media
        self.size = size
        self.file_name = file_name
