from event import Event
from ..event_type import EventType
from datetime import datetime

class UnsubscribedEvent(Event):
    def __init__(self, timestamp: datetime, user_id: str) -> None:
        super().__init__(type=EventType.UNSUBSCRIBED)
        self.user_id = user_id
