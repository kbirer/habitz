from datetime import datetime
from UI.ValuePicker import ValuePicker

class DateValuePicker(ValuePicker[datetime]):
    """UI class which picks up datetime values from user.

    Attributes:

    _formatStr -- The datetime format value which the input string must be.
    """
    _formatStr: str

    def __init__(self, inputMessage: str, formatStr: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        formatStr -- The datetime format value which the input string must be.
        """
        if not formatStr:
            raise ValueError('Datetime format string can\'t be empty')
        super().__init__(inputMessage + '. Format should be dd/mm/yyyy')
        self._formatStr = formatStr

    def _ConvertValue(self, input: str) -> datetime:
        """Implementation of abstract function to convert user input string to datetime

        Parameters:
        
        input -- The string user inputs

        Returns:
        
        Converted datetime value from input string.
        """
        return datetime.strptime(input, self._formatStr)
