from business.backend_client_factory import BackendClientFactory
from ui.multi_value_item import MultiValueItem
from ui.multi_value_picker import MultiValuePicker
from views.view import View
from views.view_action import ViewAction
from views.view_keys import MenuKeys, ViewKeys


class ListHabitsView(View):
    """Class contains logic for checking out new habit
    
    Attributes:

    ViewId -- unique view id string
    _menuItems -- menu items to select
    _mainMenu -- input picker to select from _menuItems
    """
    view_id: str = ViewKeys.list_habits
    _menu_items: list[MultiValueItem[str]] = [
        MultiValueItem[str](MenuKeys.add_new_habit, "New Habit"),
        MultiValueItem[str](MenuKeys.update_habit, "Update Habit"),
        MultiValueItem[str](MenuKeys.back, "Back"),
    ]

    _main_menu = MultiValuePicker[str](
        'Please select an option to continue', _menu_items)

    def __init__(self, starter_action: ViewAction):
        super().__init__(starter_action)

    def action(self) -> ViewAction:
        """Function to ask user necessary input for listing habits and adding new or updating existing habit
        
        Returns:

        View action to navigate
        
        """
        client = BackendClientFactory().create_backend_client()
        result = client.list_habits()
        if not result.success:
            print(result.error_message)
            return ViewAction(self.view_id, ViewKeys.main)

        for index, habit in enumerate(result.habits):  # type: ignore
            line = '{:>2} {:<50}'.format(index+1, habit.description)
            print(line)

        value = self._main_menu.PickValue()
        if value == MenuKeys.back:
            return ViewAction(self._starter_action.previous_view_id, MenuKeys.back)
        elif value == MenuKeys.add_new_habit:
            return ViewAction(self._starter_action.previous_view_id, ViewKeys.add_or_update_habit)
        elif value == MenuKeys.update_habit:
            if not result.habits or len(result.habits) == 0:
                print('There\'s no habit to update')
                return ViewAction(self._starter_action.previous_view_id, ViewKeys.add_or_update_habit)

            items: list[MultiValueItem[int]] = []
            for habit in result.habits:
                items.append(MultiValueItem[int](habit.id, habit.description))
            select_habit_menu = MultiValuePicker(
                'Please select a habit to continue', items)
            selected_habit = select_habit_menu.PickValue()
            return ViewAction(self._starter_action.previous_view_id, ViewKeys.add_or_update_habit,str(selected_habit))
        raise Exception('Unhandled menu key')
