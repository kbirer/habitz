from ui.value_picker import ValuePicker


class TextValuePicker(ValuePicker[str]):
    """UI class which picks up string values from user."""

    def __init__(self, input_message: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        """
        super().__init__(input_message)

    def _convert_value(self, input: str) -> str:
        """Implementation of abstract function to return user input string.

        Parameters:

        input -- The string user inputs

        Returns:

        Input string itself.
        """
        return input
