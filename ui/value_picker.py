from abc import abstractmethod
from datetime import datetime
from typing import Protocol, TypeVar, Union
from ui.ui_helper import UIHelper

T = TypeVar('T', bound=Union[datetime, int, str], covariant=True)

class ValuePicker(Protocol[T]):
    """Protocol class which contains common operations for picking up values from ui.
    Picks value by one of generic types (datetime,int,str)

    Attributes:

    _inputMessage -- Input message to display user while picking input value.
    """
    _input_message: str

    def __init__(self, input_message: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        """
        if not input_message:
            raise Exception(
                'inputMessage parameter can\'t be none or empty string')
        self._input_message = input_message

    def PickValue(self) -> T:
        """Function to ask user the value

        Returns:
        
        Entered value by the user from cli.
        """
        while True:
            try:
                result = input(self._input_message+"\n")
                if not result:
                    continue
                UIHelper.exit_if_commanded(result)
                return self._convert_value(result)
            except Exception as e:
                print(e)
    
    @abstractmethod
    def _convert_value(self, input: str) -> T:
        """Abstract function to convert user input to generic parameter

        Parameters:
        
        input -- The string user inputs

        Returns:
        
        Converted value from input string.
        """
        pass
