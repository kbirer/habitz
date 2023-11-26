from Business.BackendClientFactory import BackendClientFactory
from Common.HabitStreakResult import HabitStreakResult
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import ViewKeys


class HabitStreakView(View):
    """Class contains logic for querying habit streaks
    
    Attributes:

    ViewId -- unique view id string
    """
    ViewId = ViewKeys.HabitsWithLongestStreak

    def __init__(self, starterAction: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- Action data to use within this view
        
        """
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
        """Function to ask user necessary input for displaying longest streak of habits or selected habit
        
        Returns:

        View action to navigate
        
        """
        client = BackendClientFactory().CreateBackendClient()
        longestStreaksResult: HabitStreakResult
        if not self._starterAction.Data:
            longestStreaksResult = client.GetAllLongestHabitStreaks()
        else:
            longestStreaksResult = client.GetLongestHabitStreak(int(self._starterAction.Data))
        if longestStreaksResult.Success:
            for result in longestStreaksResult.HabitStreaks: # type: ignore
                print(f'{ result.HabitName: <40} {result.StreakCount :>50}')
        input('Press any key to go back to analytics view.')
        return ViewAction(self.ViewId, self._starterAction.PreviousViewId)
