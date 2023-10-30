from UI.ValuePicker import ValuePicker
from UI.UIHelper import UIHelper

class TextValuePicker(ValuePicker[str]):
    def __init__(self, inputMessage: str):
        super().__init__(inputMessage)

    def _ConvertValue(self, input: str) -> str:
        return input
