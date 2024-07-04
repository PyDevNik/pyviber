from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Button:
    """
    Message Keyboard Button Dataclass
    :param columns: Button Width in Columns
    :param rows: Button Height in Columns
    :param bg_color: Background Color of Button
    :param silent: Determine Whether the User Action is Presented in the Conversation
    :param bg_media_type: Type of the Background Media
    :param bg_media: URL for Background Media Content
    :param action_type: Type of Action Pressing the Button will Perform
    :param action_body: Action Body
    :param image: URL of Image to Place on Top of Background
    :param text: Text to be Displayed on the Button
    """
    columns: Optional[int] = None
    rows: Optional[int] = None
    bg_color: Optional[str] = None
    silent: Optional[bool] = None
    bg_media_type: Optional[str] = None
    bg_media: Optional[str] = None
    action_type: Optional[str] = None
    action_body: Optional[str] = None
    image: Optional[str] = None
    text: Optional[str] = None
    
@dataclass
class Keyboard:
    """
    Message Keyboard Dataclass
    :param buttons: List Containing All Keyboard Buttons by Order
    :param bg_color: Background Color of the Keyboard
    :param default_height: Should Height be Minimized
    :param custom_default_height: How Much Percent of Free Screen Space in Chat Should be Taken by Keyboard
    """
    buttons: List[Button]
    bg_color: Optional[str] = None
    default_height: Optional[bool] = None
    custom_default_height: Optional[int] = None