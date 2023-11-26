from Business.BackendClientFactory import BackendClientFactory
from Common.Constants import Constants
from UI.DateValuePicker import DateValuePicker
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import MenuKeys, ViewKeys


class CheckoutHabitView(View):
    """Class contains logic for checking out new habit
    
    Attributes:

    ViewId -- unique view id string
    _client -- backend client.
    """
    ViewId = ViewKeys.CheckOutHabit
    _client = BackendClientFactory().CreateBackendClient()

    def __init__(self, starterAction: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- Action data to use within this view
        
        """
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
        """Function to ask user necessary input for checking out habit
        
        Returns:

        View action to navigate
        
        """
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
