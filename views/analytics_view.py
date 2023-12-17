
from business.backend_client_factory import BackendClientFactory
from ui.multi_value_item import MultiValueItem
from ui.multi_value_picker import MultiValuePicker
from views.view import View
from views.view_action import ViewAction
from views.view_keys import MenuKeys, ViewKeys


class AnalyticsView(View):
    """Class contains logic for analyzing data to query habit streaks
    
    Attributes:

    ViewId -- unique view id string
    _menuItems -- menu items to select from.
    _menu -- Input picker to select from _menuıtems
    """
    view_id: str = ViewKeys.analytics
    _menu_items: list[MultiValueItem[str]] = [
        MultiValueItem[str](MenuKeys.habits_with_longest_streak,
                            "Habits with longest streak"),
        MultiValueItem[str](MenuKeys.longest_streak_of_selected_habit,
                            "Longest streak of selected habit")
    ]

    _menu = MultiValuePicker[str](
        '\nPlease select an option to continue\n', _menu_items)

    def __init__(self, starter_action: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- Action data to use within this view
        
        """
        super().__init__(starter_action)

    def action(self) -> ViewAction:
        """Function to ask user necessary input for displaying streaks of all habits or selected habit
        
        Returns:

        View action to navigate
        
        """
        selected_option = self._menu.PickValue()
        if selected_option == MenuKeys.longest_streak_of_selected_habit:
            list_habit_result = BackendClientFactory().create_backend_client().list_habits()
            if not list_habit_result or list_habit_result.success:
                items: list[MultiValueItem[int]] = []
                for habit in list_habit_result.habits:  # type: ignore
                    items.append(MultiValueItem[int](
                        habit.id, habit.description))
                habit_picker = MultiValuePicker(
                    'Please select a habit to continue', items)
                selected_habit_id = habit_picker.PickValue()
                return ViewAction(self.view_id, ViewKeys.habits_with_longest_streak, selected_habit_id)
            else:
                return ViewAction(self.view_id, ViewKeys.main)
        else:
            return ViewAction(self.view_id, selected_option)
