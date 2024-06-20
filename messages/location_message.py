from dataclasses import dataclass
from message import Message
from ..message_type import MessageType
from typing import Optional

@dataclass
class Location:
    lat: float
    lon: float

class LocationMessage(Message):
    def __init__(self, location: Location, tracking_data: Optional[str] = "") -> None:
        super().__init__(type=MessageType.LOCATION, tracking_data=tracking_data)
        self.location = location
