from dataclasses import dataclass

@dataclass
class BotInfo:
    id: str
    name: str
    uri: str
    icon: str
    background: str
    country: str
    webhook: str
