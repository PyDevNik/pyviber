from abc import ABC
from pyviber.message_type import MessageType
from ..keyboard import Keyboard
from typing import Optional

class Message(ABC):
    """
    Abstract Message Class
    All Message Types Should be Inherited from This Class
    :param type: Message Type
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, type: MessageType, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        self.type = type
        self.tracking_data = tracking_data
