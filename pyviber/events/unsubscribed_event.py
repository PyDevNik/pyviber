from datetime import datetime
from pyviber.events import Event
from pyviber.event_type import EventType

class UnsubscribedEvent(Event):
    """
    Unsubscribed Event
    :param timestamp: Event Timestamp
    :param user_id: User ID
    """
    def __init__(self, timestamp: datetime, user_id: str) -> None:
        super().__init__(type=EventType.UNSUBSCRIBED)
        self.user_id = user_id
