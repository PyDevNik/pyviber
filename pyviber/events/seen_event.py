from datetime import datetime
from pyviber.events import Event
from pyviber.event_type import EventType

class SeenEvent(Event):
    """
    Seen Event
    :param timestamp: Event Timestamp
    :param user_id: User ID
    :param message_token: Message Token
    """
    def __init__(self, timestamp: datetime, user_id: str, message_token: str) -> None:
        super().__init__(type=EventType.SEEN, timestamp=timestamp)
        self.user_id = user_id
        self.message_token = message_token
