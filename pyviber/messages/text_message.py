from typing import Optional
from pyviber.messages import Message
from pyviber.message_type import MessageType
from pyviber.keyboard import Keyboard

class TextMessage(Message):
    """
    Text Message
    :param text: Message Text
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, text: str, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.TEXT, keyboard=keyboard, tracking_data=tracking_data)
        self.text = text