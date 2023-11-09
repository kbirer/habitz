from Views.MainView import MainView
from Views.View import View
from Views.ViewFactory import ViewFactory
from Views.ViewKeys import MenuKeys


class ViewManager():
    _viewHistory: list[View] = [MainView()]

    def __init__(self):
        pass

    def Start(self):
        while True:
            action = self._GetCurrentView().Action()
            if action.NextViewId == MenuKeys.Back and len(self._viewHistory) > 1:
                self._viewHistory.pop()
            else:
                nextView = ViewFactory.NavigateToView(action)
                self._viewHistory.append(nextView)
                
    def _GetCurrentView(self)->View:
        return self._viewHistory[-1]