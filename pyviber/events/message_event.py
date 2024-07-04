from datetime import datetime
from pyviber.messages import Message
from pyviber.events import Event
from pyviber.event_type import EventType
from pyviber.sender import Sender

class MessageEvent(Event):
    """
    Message Event
    :param timestamp: Event Timestamp
    :param message_token: Message Token
    :param sender: Message Sender
    :param message: Message Data
    """
    def __init__(self, timestamp: datetime, message_token: str, sender: Sender, message: Message) -> None:
        super().__init__(type=EventType.MESSAGE, timestamp=timestamp)
        self.message_token = message_token
        self.sender = sender
        self.message = message
