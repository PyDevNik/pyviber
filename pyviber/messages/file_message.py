from typing import Optional
from pyviber.messages import Message
from pyviber.message_type import MessageType
from pyviber.keyboard import Keyboard

class FileMessage(Message):
    """
    File Message
    :param media: Media URL
    :param size: Media Size
    :param file_name: Media Filename
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, media: str, size: int, file_name: str, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.FILE, keyboard=keyboard, tracking_data=tracking_data)
        self.media = media
        self.size = size
        self.file_name = file_name
