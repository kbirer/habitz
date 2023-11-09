
from typing import List, Optional
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import ViewKeys


class MainView(View):
    ViewId = ViewKeys.Main
    _mainMenuItems: List[MultiValueItem[str]] = [
        MultiValueItem[str](ViewKeys.ListHabits, "List habits"),
        MultiValueItem[str](ViewKeys.ListCheckedOutHabits,"List checked out habits")
    ]

    _mainMenu = MultiValuePicker[str](
        '\nPlease select an option to continue\n', _mainMenuItems)

    def __init__(self):
        pass

    def Action(self) -> ViewAction:
        selection = self._mainMenu.PickValue()
        return ViewAction(self.ViewId, selection, None)