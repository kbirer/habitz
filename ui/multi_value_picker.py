from datetime import datetime
from typing import TypeVar, Union
from ui.multi_value_item import MultiValueItem
from ui.value_picker import ValuePicker

T = TypeVar('T', bound=Union[datetime, int, str], covariant=True)


class MultiValuePicker(ValuePicker[T]):
    """UI class which picks up a value through multiple choice.

    Attributes:

    _options -- The options to displaye user for selection.
    """
    _options: list[MultiValueItem[T]]

    def __init__(self, message:str, 
                 options: list[MultiValueItem[T]]):
        """Ctor.

        Parameters:

        message -- The message to display the user while asking for parameter.
        options -- The options to display user for selection.
        """
        super().__init__(message)
        if not options or len(options) == 0:
            print('The length of options must be greater than zero')
            exit()
        self._options = options

    def PickValue(self) -> T:
        """Function which displays options to user and asks it to pick one

        Returns:
        
        The value of the selected option.
        """
        print(self._input_message)
        for index, item in enumerate(self._options):
            print(f'{index+1} - {item._description}')
        return super().PickValue()

    def _convert_value(self, input: str) -> T:
        """Implementation of abstract function to convert user input to selected option

        Parameters:
        
        input -- The index of the selected option

        Returns:
        
        The value of the selected option.
        """
        result = int(input)
        if result < 1 or result > len(self._options):
            print('The index must be between {0} and {1}'.format(
                1, len(self._options)))
            raise Exception()
        selected_option = self._options[result-1]
        return selected_option._id
