from Business.BackendClientFactory import BackendClientFactory
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import MenuKeys, ViewKeys


class ListHabitsView(View):
    ViewId: str = ViewKeys.ListHabits
    _menuItems: list[MultiValueItem[str]] = [
        MultiValueItem[str](MenuKeys.AddNewHabit, "New Habit"),
        MultiValueItem[str](MenuKeys.UpdateHabit, "Update Habit"),
        MultiValueItem[str](MenuKeys.Back, "Back"),
    ]

    _mainMenu = MultiValuePicker[str](
        'Please select an option to continue', _menuItems)

    def __init__(self, starterAction: ViewAction):
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
        client = BackendClientFactory().CreateBackendClient()
        result = client.ListHabits()
        if not result.Success:
            print(result.ErrorMessage)
            return ViewAction(self.ViewId, ViewKeys.Main)

        for index, habit in enumerate(result.Habits):  # type: ignore
            line = '{:>2} {:<50}'.format(index+1, habit.Description)
            print(line)

        value = self._mainMenu.PickValue()
        if value == MenuKeys.Back:
            return ViewAction(self._starterAction.PreviousViewId, MenuKeys.Back)
        elif value == MenuKeys.AddNewHabit:
            return ViewAction(self._starterAction.PreviousViewId, ViewKeys.AddOrUpdateHabit)
        elif value == MenuKeys.UpdateHabit:
            if not result.Habits or len(result.Habits) == 0:
                print('There\'s no habit to update')
                return ViewAction(self._starterAction.PreviousViewId, ViewKeys.AddOrUpdateHabit)

            items: list[MultiValueItem[int]] = []
            for habit in result.Habits:
                items.append(MultiValueItem[int](habit.Id, habit.Description))
            selectHabitMenu = MultiValuePicker(
                'Please select a habit to continue', items)
            selectedHabit = selectHabitMenu.PickValue()
            return ViewAction(self._starterAction.PreviousViewId, ViewKeys.AddOrUpdateHabit,str(selectedHabit))
        raise Exception('Unhandled menu key')
