from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Button:
    columns: Optional[int] = None
    rows: Optional[int] = None
    bg_color: Optional[str] = None
    silent: Optional[bool] = None
    bg_media_type: Optional[str] = None
    bg_media: Optional[str] = None
    bg_loop: Optional[bool] = None
    action_type: Optional[str] = None
    action_body: Optional[str] = None
    image: Optional[str] = None
    text: Optional[str] = None
    
@dataclass
class Keyboard:
    buttons: List[Button]
    bg_color: Optional[str] = None
    default_height: Optional[bool] = None
    custom_default_height: Optional[int] = None
    height_scale: Optional[int] = None
    buttons_group_columns: Optional[int] = None