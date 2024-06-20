from event import Event
from ..event_type import EventType
from ..user_info import UserInfo
from datetime import datetime

class SubscribedEvent(Event):
    def __init__(self, user: UserInfo, timestamp: datetime) -> None:
        super().__init__(type=EventType.SUBSCRIBED, timestamp=timestamp)
        self.user = user
