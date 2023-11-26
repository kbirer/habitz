from dataclasses import dataclass
from typing import Any


@dataclass
class ViewAction:
    """Data class contains information for navigation between views
    
    Attributes:

    PreviousViewId -- previous view id for backwards navigation
    NextViewId -- next view id to navigate
    Data -- additional data for usage within next view if necessary
    """
    PreviousViewId: str
    NextViewId: str
    Data: Any = None
