from dataclasses import dataclass

@dataclass
class UserInfo:
    """
    Viber User Info Dataclass
    :param id: Account ID
    :param name: User Name
    :param avatar: Account Avatar URL
    :param country: User Country
    :param language: User Language
    """
    id: str
    name: str
    avatar: str
    country: str
    language: str
