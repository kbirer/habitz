
from abc import abstractmethod
from typing import Protocol
from Views.ViewAction import ViewAction


class View(Protocol):
    """Protocol class for implementing user interface logic
    
    Attributes:

    ViewId -- unique view id string
    _starterAction -- The action which this view is called with
    """
    ViewId: str
    _starterAction: ViewAction

    def __init__(self, starterAction: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- The action which this view is called with
        """
        self._starterAction = starterAction

    @abstractmethod
    def Action(self) -> ViewAction:
        """Function that runs view logic
        
        Returns:
        
        View action which contains next view to navigate
        """
        pass
