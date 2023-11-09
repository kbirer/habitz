from dataclasses import dataclass
from typing import Any


@dataclass
class ViewAction:
    PreviousViewId: str
    NextViewId: str
    Data: Any = None
