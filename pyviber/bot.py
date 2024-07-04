import requests
from typing import List, Dict, Optional, Any
from pyviber.event_type import EventType
from pyviber.message_type_handlers import MessageTypeHandlers
from pyviber.messages import *
from pyviber.sender import Sender
from pyviber.bot_info import BotInfo
from pyviber.user_info import UserInfo
from pyviber.error_codes import ErrorCode

class Bot:
    """
    Viber Bot
    :param token: Bot Token
    """
    def __init__(self, token: str) -> None:
        self._token = token
        self._event_handlers = {}
    
    def set_webhook(self, webhook: str, event_types: Optional[List[EventType]] = None) -> None:
        """
        Set Webhook
        :param webhook: Account webhook URL to receive callbacks & messages from users
        :param event_types: Indicates the types of Viber events that the account owner would like to be notified about
        """
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

    def unset_webhook(self) -> None:
        """
        Unset Webhook
        """
        self.self.set_webhook("")

    def send_message(self, receiver: str, message: Message, sender: Sender = None) -> None:
        """
        Send Message
        :param receiver: Unique Viber user ID
        :param message: Message to Send
        :param sender: Viber Message Sender (Defaults to Bot)
        """
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

        handler = MessageTypeHandlers.__getitem__(message.__name__)
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
        """
        Get Account Info
        """
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
        """
        Get User Details 
        :param id: Unique Viber user ID
        """
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
        """
        Get Online Status of Users
        :param ids: Unique Viber User IDs
        """
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
