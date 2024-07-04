from typing import Optional
from pyviber.messages import Message
from pyviber.message_type import MessageType

class StickerMessage(Message):
    """
    Sticker Message
    :param sticker_id: Sticker ID
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, sticker_id: int, keyboard: Optional[str] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.STICKER, keyboard=keyboard, tracking_data=tracking_data)
        self.sticker_id = sticker_id