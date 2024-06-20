import requests
from typing import List, Dict, Optional, Any
from event_type import EventType
from messages import Message, ContactMessage, FileMessage, \
    PictureMessage, TextMessage, VideoMessage, StickerMessage, \
    LocationMessage, UrlMessage, RichMediaMessage
from sender import Sender
from bot_info import BotInfo
from user_info import UserInfo
from error_codes import ErrorCode

class Bot:
    def __init__(self, token: str) -> None:
        self._token = token
        self._event_handlers = {}
    
    def set_webhook(self, webhook: str, event_types: Optional[List[EventType]] = None) -> Dict:
        data = {
            "url": webhook,
            **({"event_types": list(map(str, event_types))} if event_types is not None else {})
        }
        headers = {"X-Viber-Auth-Token": self._token}
        result = requests.post(
            url="https:/chatapi.viber.com/pa/set_webhook",
            headers=headers,
            data=data
        )
        if not result.json()["status"] == 0:
            raise Exception(ErrorCode(result.json()["status"]).name)
        return result

    def unset_webhook(self) -> None:
        result = self.set_webhook("")
        if not result.json()["status"] == 0:
            raise Exception(ErrorCode(result.json()["status"]).name)

    def send_message(self, sender: Sender, receiver: str, message: Message) -> None:
        data = {
            "receiver": receiver,
            "type": message.type.value,
            "sender": {
                "name": sender.name,
                "avatar": sender.avatar
            },
            "keyboard": message.keyboard,
            "tracking_data": message.tracking_data
        }

        message_type_handlers = {
            TextMessage: lambda m: {"text": m.text},
            FileMessage: lambda m: {"media": m.media, "size": m.size, "file_name": m.file_name},
            PictureMessage: lambda m: {"text": m.text, "media": m.media, "thumbnail": m.thumbnail if m.thumbnail else None},
            VideoMessage: lambda m: {"text": m.text, "media": m.media, "size": m.size, "duration": m.duration if m.duration else None, "thumbnail": m.thumbnail if m.thumbnail else None},
            ContactMessage: lambda m: {"contact": {"name": m.contact.name, "phone_number": m.contact.phone_number}},
            LocationMessage: lambda m: {"location": {"lat": m.location.lat, "lon": m.location.lon}},
            UrlMessage: lambda m: {"media": m.media},
            RichMediaMessage: lambda m: {"rich_media": "Not implemented"},
            StickerMessage: lambda m: {"sticker_id": m.sticker_id}
        }

        handler = message_type_handlers.get(type(message))
        if handler:
            data.update(handler(message))

        headers = {"X-Viber-Auth-Token": self._token}
        result = requests.post(
            url="https:/chatapi.viber.com/pa/send_message",
            headers=headers,
            data=data
        )
        if not result.json()["status"] == 0:
            raise Exception(ErrorCode(result.json()["status"]).name)
        return result
    
    def get_account_info(self) -> BotInfo:
        headers = {"X-Viber-Auth-Token": self._token}
        result = requests.post(
            url="https:/chatapi.viber.com/pa/get_account_info",
            headers=headers,
            data={}
        )
        if not result.json()["status"] == 0:
            raise Exception(ErrorCode(result.json()["status"]).name)
        return BotInfo(**result)
    
    def get_user_details(self, id: str) -> UserInfo:
        headers = {"X-Viber-Auth-Token": self._token}
        result = requests.post(
            url="https:/chatapi.viber.com/pa/get_user_details",
            headers=headers,
            data={"id": id}
        )
        if not result.json()["status"] == 0:
            raise Exception(ErrorCode(result.json()["status"]).name)
        return UserInfo(**result["user"])

    def get_online(self, ids: List[str]) -> List[Dict]:
        headers = {"X-Viber-Auth-Token": self._token}
        result = requests.post(
            url="https:/chatapi.viber.com/pa/get_online",
            headers=headers,
            data={"ids": ids}
        )
        if not result.json()["status"] == 0:
            raise Exception(ErrorCode(result.json()["status"]).name)
        return result["users"]

    def event(self, event_type: str):
        def decorator(func):
            if event_type not in self._event_handlers:
                self._event_handlers[event_type] = []
            self._event_handlers[event_type].append(func)
            return func
        return decorator

    def handle_event(self, event: Dict) -> Any:
        if event["event"] in self._event_handlers: 
            self._event_handlers[event["event"]](event)
