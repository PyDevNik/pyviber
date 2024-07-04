from dataclasses import dataclass
from typing import Optional
from pyviber.messages import Message
from pyviber.message_type import MessageType
from pyviber.keyboard import Keyboard

@dataclass
class Location:
    """
    Location Dataclass
    :param lat: Latitude
    :param lon: Longitude
    """
    lat: float
    lon: float

class LocationMessage(Message):
    """
    Location Message
    :param location: Location
    :param keyboard: Optional Message Keyboard
    :param tracking_data: Tracking Data
    """
    def __init__(self, location: Location, keyboard: Optional[Keyboard] = None, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.LOCATION, keyboard=keyboard, tracking_data=tracking_data)
        self.location = location

