
from abc import abstractmethod
from typing import Protocol
from views.view_action import ViewAction


class View(Protocol):
    """Protocol class for implementing user interface logic
    
    Attributes:

    ViewId -- unique view id string
    _starterAction -- The action which this view is called with
    """
    view_id: str
    _starter_action: ViewAction

    def __init__(self, starter_action: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- The action which this view is called with
        """
        self._starter_action = starter_action

    @abstractmethod
    def action(self) -> ViewAction:
        """Function that runs view logic
        
        Returns:
        
        View action which contains next view to navigate
        """
        pass
