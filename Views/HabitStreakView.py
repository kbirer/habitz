from Business.BackendClientFactory import BackendClientFactory
from Common.HabitStreakResult import HabitStreakResult
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import ViewKeys


class HabitStreakView(View):
    ViewId = ViewKeys.HabitsWithLongestStreak

    def __init__(self, starterAction: ViewAction):
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
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
