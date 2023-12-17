from ui.multi_value_item import MultiValueItem
from ui.multi_value_picker import MultiValuePicker
from views.view import View
from views.view_action import ViewAction
from views.view_keys import ViewKeys


class MainView(View):
    """Class contains main menu logic
    
    Attributes:

    ViewId -- unique view id string
    _menuItems -- menu items to select
    _mainMenu -- input picker to select from _menuItems
    """
    view_id = ViewKeys.main
    _main_menu_items: list[MultiValueItem[str]] = [
        MultiValueItem[str](ViewKeys.list_habits, "List habits"),
        MultiValueItem[str](ViewKeys.list_checked_out_habits,"List checked out habits"),
        MultiValueItem[str](ViewKeys.check_out_habit,"Checkout new habit"),
        MultiValueItem[str](ViewKeys.analytics,"Analytics")
    ]

    _main_menu = MultiValuePicker[str](
        '\nPlease select an option to continue\n', _main_menu_items)

    def __init__(self):
        pass

    def action(self) -> ViewAction:
        selection = self._main_menu.PickValue()
        return ViewAction(self.view_id, selection, None)
