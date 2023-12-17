from ui.value_picker import ValuePicker

class NumberValuePicker(ValuePicker[int]):
    """UI class which picks up integer values from user."""

    def __init__(self, input_message: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        """
        super().__init__(input_message)

    def _convert_value(self, input: str) -> int:
        """Implementation of abstract function to convert user input string to integer

        Parameters:
        
        input -- The string user inputs

        Returns:
        
        Converted integer value from input string.
        """
        return int(input)
