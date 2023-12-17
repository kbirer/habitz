
from business.backend_client_factory import BackendClientFactory
from common.constants import Constants
from ui.date_value_picker import DateValuePicker
from ui.multi_value_item import MultiValueItem
from ui.multi_value_picker import MultiValuePicker
from views.view import View
from views.view_action import ViewAction
from views.view_keys import MenuKeys, ViewKeys


class ListCheckedoutHabitsView(View):
    """Class contains logic for listing, adding or updating habits
    
    Attributes:

    ViewId -- unique view id string
    _menuItems -- menu items to select
    _mainMenu -- input picker to select from _menuItems
    _startDatePicker -- start date input picker
    _endDatePicker -- end date input picker
    """
    view_id: str = ViewKeys.list_checked_out_habits

    _menu_items: list[MultiValueItem[str]] = [
        MultiValueItem[str](ViewKeys.check_out_habit, "Checkout habit"),
        MultiValueItem[str](MenuKeys.back, "Back")
    ]

    _main_menu = MultiValuePicker[str](
        'Please select an option to continue', _menu_items)

    _start_date_picker = DateValuePicker(
        'Please select the start date', Constants.date_picker_format)
    _end_date_picker = DateValuePicker(
        'Please select the start date', Constants.date_picker_format)

    def action(self) -> ViewAction:
        """Function to ask user necessary input for querying checked out habits
        
        Returns:

        View action to navigate
        
        """
        client = BackendClientFactory().create_backend_client()
        start_date = self._start_date_picker.PickValue()
        end_date = self._end_date_picker.PickValue()
        result = client.list_checkedout_habits(start_date, end_date)
        if not result.success:
            return ViewAction(self._starter_action.previous_view_id, MenuKeys.back)
        previous_habit_id=0
        print(f'Checked out habits for {start_date} and {end_date}')
        for index, checkedout_habit in enumerate(result.checkedout_habits):  # type: ignore
            if previous_habit_id != checkedout_habit.habit_id:
                print(f'{index+1 : <5} { checkedout_habit.habit_description: <40} {checkedout_habit.creation_date.strftime("%Y-%m-%d") :>50}')
                previous_habit_id = checkedout_habit.habit_id
            else:
                print(f'{index+1 : <5} { "": <40} {checkedout_habit.creation_date.strftime("%Y-%m-%d") :>50}')
        value = self._main_menu.PickValue()
        return ViewAction(self.view_id, value)
