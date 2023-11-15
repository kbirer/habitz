from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import ViewKeys


class MainView(View):
    ViewId = ViewKeys.Main
    _mainMenuItems: list[MultiValueItem[str]] = [
        MultiValueItem[str](ViewKeys.ListHabits, "List habits"),
        MultiValueItem[str](ViewKeys.ListCheckedOutHabits,"List checked out habits"),
        MultiValueItem[str](ViewKeys.CheckOutHabit,"Checkout new habit"),
        MultiValueItem[str](ViewKeys.Analytics,"Analytics")
    ]

    _mainMenu = MultiValuePicker[str](
        '\nPlease select an option to continue\n', _mainMenuItems)

    def __init__(self):
        pass

    def Action(self) -> ViewAction:
        selection = self._mainMenu.PickValue()
        return ViewAction(self.ViewId, selection, None)
