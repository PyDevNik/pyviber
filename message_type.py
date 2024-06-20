from enum import Enum

class MessageType(Enum):
    TEXT = "text"
    PICTURE = "picture"
    VIDEO = "video"
    FILE = "file"
    LOCATION = "location"
    CONTACT = "contact"
    STICKER = "sticker"
    RICH_MEDIA = "rich_media"
