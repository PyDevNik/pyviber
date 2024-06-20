from dataclasses import dataclass
from message import Message
from ..message_type import MessageType
from typing import Optional

@dataclass
class Contact:
    name: str
    phone_number: str

class ContactMessage(Message):
    def __init__(self, contact: Contact, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.CONTACT, tracking_data=tracking_data)
        self.contact = contact
