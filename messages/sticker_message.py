from message import Message
from ..message_type import MessageType
from typing import Optional

class StickerMessage(Message):
    def __init__(self, sticker_id: int, keyboard: Optional[str] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.STICKER, keyboard=keyboard, tracking_data=tracking_data)
        self.sticker_id = sticker_id