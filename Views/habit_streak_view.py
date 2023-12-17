from business.backend_client_factory import BackendClientFactory
from common.habit_streak_result import HabitStreakResult
from views.view import View
from views.view_action import ViewAction
from views.view_keys import ViewKeys


class HabitStreakView(View):
    """Class contains logic for querying habit streaks
    
    Attributes:

    ViewId -- unique view id string
    """
    view_id = ViewKeys.habits_with_longest_streak

    def __init__(self, starterAction: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- Action data to use within this view
        
        """
        super().__init__(starterAction)

    def action(self) -> ViewAction:
        """Function to ask user necessary input for displaying longest streak of habits or selected habit
        
        Returns:

        View action to navigate
        
        """
        client = BackendClientFactory().create_backend_client()
        longest_streaks_result: HabitStreakResult
        if not self._starter_action.data:
            longest_streaks_result = client.get_all_longest_habit_streaks()
        else:
            longest_streaks_result = client.get_longest_habit_streak(int(self._starter_action.data))
        if longest_streaks_result.success:
            for result in longest_streaks_result.habit_streaks: # type: ignore
                print(f'{ result.habit_name: <40} {result.streak_count :>50}')
        input('Press any key to go back to analytics view.')
        return ViewAction(self.view_id, self._starter_action.previous_view_id)
