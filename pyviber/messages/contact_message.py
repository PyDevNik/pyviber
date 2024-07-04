from dataclasses import dataclass
from pyviber.messages import Message
from pyviber.message_type import MessageType
from pyviber.keyboard import Keyboard
from typing import Optional

@dataclass
class Contact:
    """
    Contact Dataclass
    :param name: Account Name
    :param phone_number: User Phone Number
    """
    name: str
    phone_number: str

class ContactMessage(Message):
    """
    Contact Message
    :param contact: User Contact
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, contact: Contact, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.CONTACT, keyboard=keyboard, tracking_data=tracking_data)
        self.contact = contact
