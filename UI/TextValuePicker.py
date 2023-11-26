from UI.ValuePicker import ValuePicker
from UI.UIHelper import UIHelper

class TextValuePicker(ValuePicker[str]):
    """UI class which picks up string values from user."""

    def __init__(self, inputMessage: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        """
        super().__init__(inputMessage)

    def _ConvertValue(self, input: str) -> str:
        """Implementation of abstract function to return user input string.

        Parameters:
        
        input -- The string user inputs

        Returns:
        
        Input string itself.
        """
        return input
