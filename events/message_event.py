from event import Event
from ..event_type import EventType
from datetime import datetime
from ..sender import Sender

class MessageEvent(Event):
    def __init__(self, timestamp: datetime, message_token: str, sender: Sender, message: str) -> None:
        super().__init__(type=EventType.MESSAGE, timestamp=timestamp)
        self.message_token = message_token
        self.sender = sender
        self.message = message
