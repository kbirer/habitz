
from Business.BackendClientFactory import BackendClientFactory
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import MenuKeys, ViewKeys


class AnalyticsView(View):
    """Class contains logic for analyzing data to query habit streaks
    
    Attributes:

    ViewId -- unique view id string
    _menuItems -- menu items to select from.
    _menu -- Input picker to select from _menuıtems
    """
    ViewId: str = ViewKeys.Analytics
    _menuItems: list[MultiValueItem[str]] = [
        MultiValueItem[str](MenuKeys.HabitsWithLongestStreak,
                            "Habits with longest streak"),
        MultiValueItem[str](MenuKeys.LongestStreakOfSelectedHabit,
                            "Longest streak of selected habit")
    ]

    _menu = MultiValuePicker[str](
        '\nPlease select an option to continue\n', _menuItems)

    def __init__(self, starterAction: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- Action data to use within this view
        
        """
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
        """Function to ask user necessary input for displaying streaks of all habits or selected habit
        
        Returns:

        View action to navigate
        
        """
        selectedOption = self._menu.PickValue()
        if selectedOption == MenuKeys.LongestStreakOfSelectedHabit:
            listHabitResult = BackendClientFactory().CreateBackendClient().ListHabits()
            if not listHabitResult or listHabitResult.Success:
                items: list[MultiValueItem[int]] = []
                for habit in listHabitResult.Habits:  # type: ignore
                    items.append(MultiValueItem[int](
                        habit.Id, habit.Description))
                habitPicker = MultiValuePicker(
                    'Please select a habit to continue', items)
                selectedHabitId = habitPicker.PickValue()
                return ViewAction(self.ViewId, ViewKeys.HabitsWithLongestStreak, selectedHabitId)
            else:
                return ViewAction(self.ViewId, ViewKeys.Main)
        else:
            return ViewAction(self.ViewId, selectedOption)
