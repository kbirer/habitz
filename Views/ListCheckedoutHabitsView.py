
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
        MultiValueItem[str](MenuKeys.CheckOutHabit, "Checkout habit"),
        MultiValueItem[str](MenuKeys.DeleteCheckedOutHabit,
                            "Delete checked out habit"),
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
        previousHabitId: int
        line: str = '{:>2} {:<20} {:<20}'
        print(f'Checked out fabits for {startDate} and {endDate}')
        for index, checkedoutHabit in enumerate(result.CheckedoutHabits):  # type: ignore
            if previousHabitId != checkedoutHabit.HabitId:
                print(line.format(index+1, checkedoutHabit.HabitDescription, checkedoutHabit.CreationDate))
            else:
                print(line.format('{:>2} {:<20} {:<20}'.format(
                index+1, '', checkedoutHabit.CreationDate)))
        value = self._mainMenu.PickValue()
            #if value == MenuKeys.Back:
        return ViewAction(self._starterAction.PreviousViewId, MenuKeys.Back)
