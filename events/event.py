from abc import ABC
from ..event_type import EventType
from datetime import datetime

class Event(ABC):
    def __init__(self, type: EventType, timestamp: datetime) -> None:
        self.type = type
        self.timestamp = timestamp