from typing import Optional
from pyviber.messages import Message
from pyviber.message_type import MessageType
from pyviber.keyboard import Keyboard

class UrlMessage(Message):
    """
    URL Message
    :param media: Media URL
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, media: str, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.URL, keyboard=keyboard, tracking_data=tracking_data)
        self.media = media