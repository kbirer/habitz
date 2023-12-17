from business.backend_client_factory import BackendClientFactory
from common.periodicity import Periodicity
from ui.number_value_picker import NumberValuePicker
from ui.text_value_picker import TextValuePicker
from ui.multi_value_item import MultiValueItem
from ui.multi_value_picker import MultiValuePicker
from views.view import View
from views.view_action import ViewAction
from views.view_keys import MenuKeys, ViewKeys


class AddOrUpdateHabitView(View):
    """Class contains logic for updating and adding new habit. Derives from View

    Attributes:

    ViewId -- unique view id string
    _periodicityMenu -- Periods to select
    _textValuePicker -- Input picker for habit name
    _timesValuePicker -- Input picker for time habit
    _backendClient -- Backend client
    """

    view_id: str = ViewKeys.add_or_update_habit
    _periodicity_menu = MultiValuePicker('Please select periodicity', [
        MultiValueItem(1, 'Day'),
        MultiValueItem(2, 'Week'),
        MultiValueItem(3, 'Month'),
        MultiValueItem(4, 'Year'),
    ])
    _text_value_picker = TextValuePicker('Please enter habit description')
    _times_value_picker = NumberValuePicker(
        'Please enter how many times habit should be completed on given period')
    _backend_client = BackendClientFactory().create_backend_client()

    def __init__(self, starter_action: ViewAction):
        """Ctor

        Parameters:

        starterAction -- Action data to use within this view

        """
        super().__init__(starter_action)

    def action(self) -> ViewAction:
        """Function to ask user necessary input for adding or updating habit

        Returns:

        View action to navigate

        """
        selected_habit_id: int = 0
        client = BackendClientFactory().create_backend_client()
        if self._starter_action.data:
            selected_habit_id = int(self._starter_action.data)
            selected_habit_result = client.get_habit_by_id(selected_habit_id)
            if not selected_habit_result.success or not selected_habit_result.selected_habit:
                return ViewAction(self.view_id, MenuKeys.back)
            selected_habit = selected_habit_result.selected_habit
            print('Habit you selected is:', end='\n')
            print(selected_habit.description, end='\n')
        self._save_new_habit_information(selected_habit_id)
        return ViewAction(self.view_id, MenuKeys.back)

    def _save_new_habit_information(self, existingHabitId: int):
        self._backend_client.save_habit(
            self._text_value_picker.PickValue(),
            Periodicity(self._periodicity_menu.PickValue()),
            self._times_value_picker.PickValue(), existingHabitId)
