from dataclasses import dataclass

@dataclass
class UserInfo:
    id: str
    name: str
    avatar: str
    country: str
    language: str
