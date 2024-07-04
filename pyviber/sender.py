from dataclasses import dataclass

@dataclass
class Sender:
    """
    Message Sender Dataclass
    :param name: Sender Name
    :param avatar: Sender Avatar URL
    """
    name: str
    avatar: str