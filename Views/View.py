
from abc import abstractmethod
from typing import Protocol
from Views.ViewAction import ViewAction


class View(Protocol):
    ViewId: str
    _starterAction: ViewAction

    def __init__(self, starterAction: ViewAction):
        self._starterAction = starterAction

    @abstractmethod
    def Action(self) -> ViewAction:
        pass
