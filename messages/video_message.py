from message import Message
from ..message_type import MessageType
from typing import Optional

class VideoMessage(Message):
    def __init__(self, text: str, media: str, size: int, duration: Optional[int] = None, thumbnail: Optional[str] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.VIDEO, tracking_data=tracking_data)
        self.text = text
        self.media = media
        self.size = size
        self.duration = duration
        self.thumbnail = thumbnail
