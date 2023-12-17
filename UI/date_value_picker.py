from datetime import datetime
from ui.value_picker import ValuePicker

class DateValuePicker(ValuePicker[datetime]):
    """UI class which picks up datetime values from user.

    Attributes:

    _formatStr -- The datetime format value which the input string must be.
    """
    _formatStr: str

    def __init__(self, input_message: str, format_str: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        formatStr -- The datetime format value which the input string must be.
        """
        if not format_str:
            raise ValueError('Datetime format string can\'t be empty')
        super().__init__(input_message + '. Format should be dd/mm/yyyy')
        self._formatStr = format_str

    def _convert_value(self, input: str) -> datetime:
        """Implementation of abstract function to convert user input string to datetime

        Parameters:
        
        input -- The string user inputs

        Returns:
        
        Converted datetime value from input string.
        """
        return datetime.strptime(input, self._formatStr)
