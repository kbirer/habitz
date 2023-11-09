from UI.ValuePicker import ValuePicker

class NumberValuePicker(ValuePicker[int]):

    def __init__(self, inputMessage: str):
        super().__init__(inputMessage)

    def _ConvertValue(self, input: str) -> int:
        return int(input)
