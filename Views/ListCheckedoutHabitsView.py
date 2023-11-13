
from Business.BackendClientFactory import BackendClientFactory
from Common.Constants import Constants
from UI.DateValuePicker import DateValuePicker
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import MenuKeys, ViewKeys


class ListCheckedoutHabitsView(View):
    ViewId: str = ViewKeys.ListCheckedOutHabits

    _menuItems: list[MultiValueItem[str]] = [
        MultiValueItem[str](ViewKeys.CheckOutHabit, "Checkout habit"),
        MultiValueItem[str](MenuKeys.Back, "Back")
    ]

    _mainMenu = MultiValuePicker[str](
        'Please select an option to continue', _menuItems)

    _startDatePicker = DateValuePicker(
        'Please select the start date', Constants.DatePickerFormat)
    _endDatePicker = DateValuePicker(
        'Please select the start date', Constants.DatePickerFormat)

    def Action(self) -> ViewAction:
        client = BackendClientFactory().CreateBackendClient()
        startDate = self._startDatePicker.PickValue()
        endDate = self._endDatePicker.PickValue()
        result = client.ListCheckedoutHabits(startDate, endDate)
        if not result.Success:
            return ViewAction(self._starterAction.PreviousViewId, MenuKeys.Back)
        previousHabitId=0
        print(f'Checked out fabits for {startDate} and {endDate}')
        for index, checkedoutHabit in enumerate(result.CheckedoutHabits):  # type: ignore
            if previousHabitId != checkedoutHabit.HabitId:
                print(f'{index+1 : <5} { checkedoutHabit.HabitDescription: <40} {checkedoutHabit.CreationDate.strftime("%Y-%m-%d") :>50}')
                previousHabitId = checkedoutHabit.HabitId
            else:
                print(f'{index+1 : <5} { "": <40} {checkedoutHabit.CreationDate.strftime("%Y-%m-%d") :>50}')
        value = self._mainMenu.PickValue()
        return ViewAction(self.ViewId, value)
