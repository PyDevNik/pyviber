from event import Event
from ..event_type import EventType
from ..user_info import UserInfo
from datetime import datetime

class ConversationStartedEvent(Event):
    def __init__(self, timestamp: datetime, user: UserInfo, subscribed: bool, context: str) -> None:
        super().__init__(type=EventType.CONVERSATION_STARTED, timestamp=timestamp)
        self.user = user
        self.subscribed = subscribed
        self.context = context
