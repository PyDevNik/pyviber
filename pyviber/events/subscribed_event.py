from datetime import datetime
from pyviber.events import Event
from pyviber.event_type import EventType
from pyviber.user_info import UserInfo

class SubscribedEvent(Event):
    """
    Subscribed Event
    :param timestamp: Event Timestamp
    :param user: User Account Info
    """
    def __init__(self, timestamp: datetime, user: UserInfo) -> None:
        super().__init__(type=EventType.SUBSCRIBED, timestamp=timestamp)
        self.user = user
