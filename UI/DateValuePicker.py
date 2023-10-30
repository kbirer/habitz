from datetime import datetime
from UI.ValuePicker import ValuePicker

class DateValuePicker(ValuePicker[datetime]):
    _formatStr: str

    def __init__(self, inputMessage: str, formatStr: str):
        if not formatStr:
            raise ValueError('Datetime format string can\'t be empty')
        super().__init__(inputMessage + '. Format should be dd/mm/yyyy')
        self._formatStr = formatStr

    def _ConvertValue(self, input: str) -> datetime:
        return datetime.strptime(input, self._formatStr)
