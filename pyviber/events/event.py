from abc import ABC
from datetime import datetime
from pyviber.event_type import EventType

class Event(ABC):
    """
    Abstract Event Class
    All Event Types Should be Inherited from This Class
    :param type: Event Type
    :param timestamp: Event Timestamp
    """
    def __init__(self, type: EventType, timestamp: datetime) -> None:
        self.type = type
        self.timestamp = timestamp