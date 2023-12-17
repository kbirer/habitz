from views.main_view import MainView
from views.view import View
from views.view_factory import ViewFactory
from views.view_keys import MenuKeys


class ViewManager():
    """Class which manages the navigation between views
    
    Attributes:

    _viewHistory -- A stack contains view history for backward navigation
    """

    _view_history: list[View] = [MainView()]

    def __init__(self):
        """Ctor"""
        pass

    def start(self):
        """Runs view logic and navigation through user selections"""
        while True:
            action = self._get_current_view().action()
            if action.next_view_id == MenuKeys.back and len(self._view_history) > 1:
                self._view_history.pop()
            else:
                next_view = ViewFactory.navigate_to_view(action)
                self._view_history.append(next_view)
                
    def _get_current_view(self)->View:
        """Function which pops view from _viewHistory stack for backwards navigation
        
        Returns:

        Previous view.
        
        """
        return self._view_history[-1]