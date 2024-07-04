from typing import Optional
from pyviber.messages import Message
from pyviber.message_type import MessageType
from pyviber.keyboard import Keyboard

class PictureMessage(Message):
    """
    Picture Message
    :param text: Message Text
    :param media: Media URL
    :param thumbnail: Optional Media Thumbnail
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, text: str, media: str, thumbnail: Optional[str] = None, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.PICTURE, keyboard=keyboard, tracking_data=tracking_data)
        self.text = text
        self.media = media
        self.thumbnail = thumbnail
