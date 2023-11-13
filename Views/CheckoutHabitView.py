from Business.BackendClientFactory import BackendClientFactory
from Common.Constants import Constants
from UI.DateValuePicker import DateValuePicker
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import MenuKeys, ViewKeys


class CheckoutHabitView(View):
    ViewId = ViewKeys.CheckOutHabit
    _client = BackendClientFactory().CreateBackendClient()

    def __init__(self, starterAction: ViewAction):
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
        listHabitResult = self._client.ListHabits()
        if not listHabitResult.Success:
            return ViewAction(self._starterAction.PreviousViewId, MenuKeys.Back)

        habitSelectPickerItems: list[MultiValueItem[int]] = []
        for habit in listHabitResult.Habits:  # type: ignore
            habitSelectPickerItems.append(
                MultiValueItem(habit.Id, habit.Description))

        habitPicker = MultiValuePicker(
            'Please select a habit', habitSelectPickerItems)
        selectedHabitId = habitPicker.PickValue()
        datePicker = DateValuePicker(
            'Please enter checkout date', Constants.DatePickerFormat)
        checkoutDate = datePicker.PickValue()

        self._client.CheckoutHabit(selectedHabitId, checkoutDate)

        return ViewAction(self._starterAction.PreviousViewId, MenuKeys.Back)
