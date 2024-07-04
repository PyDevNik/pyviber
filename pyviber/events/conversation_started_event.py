from datetime import datetime
from pyviber.events import Event
from pyviber.event_type import EventType
from pyviber.user_info import UserInfo

class ConversationStartedEvent(Event):
    """
    Conversation Started Event
    :param timestam: Event Timestamp
    :param user: User Info
    :param subscribed: Whether the User is Already Subscribed
    :param context: Additional Context
    """
    def __init__(self, timestamp: datetime, user: UserInfo, subscribed: bool, context: str) -> None:
        super().__init__(type=EventType.CONVERSATION_STARTED, timestamp=timestamp)
        self.user = user
        self.subscribed = subscribed
        self.context = context
