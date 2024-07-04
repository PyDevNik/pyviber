from enum import Enum

class EventType(Enum):
    """
    Event Type Enum
    """
    SUBSCRIBED = "subscribed"
    UNSUBSCRIBED = "unsubscribed"
    DELIVERED = "delivered"
    SEEN = "seen"
    FAILED = "failed"
    CONVERSATION_STARTED = "conversation_started"
    MESSAGE = "message"
