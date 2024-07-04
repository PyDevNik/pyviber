from enum import Enum
from pyviber.messages import *

class MessageTypeHandlers(Enum):
    """
    Message Type Handlers Enum
    """
    TextMessage = lambda m: {"text": m.text},
    FileMessage = lambda m: {"media": m.media, "size": m.size, "file_name": m.file_name},
    PictureMessage = lambda m: {"text": m.text, "media": m.media, "thumbnail": m.thumbnail if m.thumbnail else None},
    VideoMessage = lambda m: {"text": m.text, "media": m.media, "size": m.size, "duration": m.duration if m.duration else None, "thumbnail": m.thumbnail if m.thumbnail else None},
    ContactMessage = lambda m: {"contact": {"name": m.contact.name, "phone_number": m.contact.phone_number}},
    LocationMessage = lambda m: {"location": {"lat": m.location.lat, "lon": m.location.lon}},
    UrlMessage = lambda m: {"media": m.media},
    RichMediaMessage = lambda m: {"rich_media": "Not implemented"},
    StickerMessage = lambda m: {"sticker_id": m.sticker_id}