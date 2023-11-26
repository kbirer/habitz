from abc import abstractmethod
from datetime import datetime
from typing import Protocol, TypeVar, Union
from UI.UIHelper import UIHelper

T = TypeVar('T', bound=Union[datetime, int, str], covariant=True)

class ValuePicker(Protocol[T]):
    """Protocol class which contains common operations for picking up values from ui.
    Picks value by one of generic types (datetime,int,str)

    Attributes:

    _inputMessage -- Input message to display user while picking input value.
    """
    _inputMessage: str

    def __init__(self, inputMessage: str):
        """Ctor

        Parameters:

        inputMessage -- Input message to display user while picking input value.
        """
        if not inputMessage:
            raise Exception(
                'inputMessage parameter can\'t be none or empty string')
        self._inputMessage = inputMessage

    def PickValue(self) -> T:
        """Function to ask user the value

        Returns:
        
        Entered value by the user from cli.
        """
        while True:
            try:
                result = input(self._inputMessage+"\n")
                if not result:
                    continue
                UIHelper.ExitIfCommanded(result)
                return self._ConvertValue(result)
            except Exception as e:
                print(e)
    
    @abstractmethod
    def _ConvertValue(self, input: str) -> T:
        """Abstract function to convert user input to generic parameter

        Parameters:
        
        input -- The string user inputs

        Returns:
        
        Converted value from input string.
        """
        pass
