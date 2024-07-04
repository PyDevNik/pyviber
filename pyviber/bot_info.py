from dataclasses import dataclass

@dataclass
class BotInfo:
    """
    Bot Info Dataclass
    :param id: Bot Account ID
    :param name: Bot Account Name
    :param uri: Unique URI of the Account
    :param icon: Account icon URL
    :param background: Conversation background URL
    :param country: Bot Account Country
    :param webhook: Account Registered Webhook URL
    """
    id: str
    name: str
    uri: str
    icon: str
    background: str
    country: str
    webhook: str
