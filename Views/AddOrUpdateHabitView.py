from Business.BackendClientFactory import BackendClientFactory
from Common.Habit import Habit
from Common.Periodicity import Periodicity
from UI.NumberValuePicker import NumberValuePicker
from UI.TextValuePicker import TextValuePicker
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker
from Views.View import View
from Views.ViewAction import ViewAction
from Views.ViewKeys import MenuKeys, ViewKeys


class AddOrUpdateHabitView(View):
    ViewId: str = ViewKeys.AddOrUpdateHabit
    _periodicityMenu = MultiValuePicker('Please select periodicity', [
        MultiValueItem(1, 'Day'),
        MultiValueItem(2, 'Week'),
        MultiValueItem(3, 'Month'),
        MultiValueItem(4, 'Year'),
    ])
    _textValuePicker = TextValuePicker('Please enter habit description')
    _timesValuePicker = NumberValuePicker(
        'Please enter how many times habit should be completed on given period')
    _backendClient=BackendClientFactory().CreateBackendClient()

    def __init__(self, starterAction: ViewAction):
        super().__init__(starterAction)

    def Action(self) -> ViewAction:
        selectedHabitId: int = 0
        client = BackendClientFactory().CreateBackendClient()
        if self._starterAction.Data:
            selectedHabitId = int(self._starterAction.Data)
            selectedHabitResult = client.GetHabitById(selectedHabitId)
            if not selectedHabitResult.Success or not selectedHabitResult.SelectedHabit:
                return ViewAction(self.ViewId, MenuKeys.Back)
            selectedHabit = selectedHabitResult.SelectedHabit
            print('Habit you selected is:', end='\n')
            print(selectedHabit.Description, end='\n')
        self._SaveNewHabitInformation(selectedHabitId)
        return ViewAction(self.ViewId, MenuKeys.Back)

    def _SaveNewHabitInformation(self, existingHabitId: int):
        self._backendClient.SaveHabit(
            self._textValuePicker.PickValue(),
            Periodicity(self._periodicityMenu.PickValue()),
            self._timesValuePicker.PickValue(),existingHabitId)
