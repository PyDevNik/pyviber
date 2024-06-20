from event import Event
from ..event_type import EventType
from datetime import datetime

class SeenEvent(Event):
    def __init__(self, timestamp: datetime, user_id: str, message_token: str) -> None:
        super().__init__(type=EventType.SEEN, timestamp=timestamp)
        self.user_id = user_id
        self.message_token = message_token
