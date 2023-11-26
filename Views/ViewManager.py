from Views.MainView import MainView
from Views.View import View
from Views.ViewFactory import ViewFactory
from Views.ViewKeys import MenuKeys


class ViewManager():
    """Class which manages the navigation between views
    
    Attributes:

    _viewHistory -- A stack contains view history for backward navigation
    """

    _viewHistory: list[View] = [MainView()]

    def __init__(self):
        """Ctor"""
        pass

    def Start(self):
        """Runs view logic and navigation through user selections"""
        while True:
            action = self._GetCurrentView().Action()
            if action.NextViewId == MenuKeys.Back and len(self._viewHistory) > 1:
                self._viewHistory.pop()
            else:
                nextView = ViewFactory.NavigateToView(action)
                self._viewHistory.append(nextView)
                
    def _GetCurrentView(self)->View:
        """Function which pops view from _viewHistory stack for backwards navigation
        
        Returns:

        Previous view.
        
        """
        return self._viewHistory[-1]