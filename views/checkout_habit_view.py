from business.backend_client_factory import BackendClientFactory
from common.constants import Constants
from ui.date_value_picker import DateValuePicker
from ui.multi_value_item import MultiValueItem
from ui.multi_value_picker import MultiValuePicker
from views.view import View
from views.view_action import ViewAction
from views.view_keys import MenuKeys, ViewKeys


class CheckoutHabitView(View):
    """Class contains logic for checking out new habit
    
    Attributes:

    ViewId -- unique view id string
    _client -- backend client.
    """
    view_id = ViewKeys.check_out_habit
    _client = BackendClientFactory().create_backend_client()

    def __init__(self, starter_action: ViewAction):
        """Ctor
        
        Parameters:

        starterAction -- Action data to use within this view
        
        """
        super().__init__(starter_action)

    def action(self) -> ViewAction:
        """Function to ask user necessary input for checking out habit
        
        Returns:

        View action to navigate
        
        """
        list_habit_result = self._client.list_habits()
        if not list_habit_result.success:
            return ViewAction(self._starter_action.previous_view_id, MenuKeys.back)

        habit_select_picker_items: list[MultiValueItem[int]] = []
        for habit in list_habit_result.habits:  # type: ignore
            habit_select_picker_items.append(
                MultiValueItem(habit.id, habit.description))

        habit_picker = MultiValuePicker(
            'Please select a habit', habit_select_picker_items)
        selected_habit_id = habit_picker.PickValue()
        date_picker = DateValuePicker(
            'Please enter checkout date', Constants.date_picker_format)
        checkout_date = date_picker.PickValue()

        self._client.checkout_habit(selected_habit_id, checkout_date)

        return ViewAction(self._starter_action.previous_view_id, MenuKeys.back)
