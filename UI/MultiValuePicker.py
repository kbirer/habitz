from datetime import datetime
from typing import List, TypeVar, Union
from UI.MultiValueItem import MultiValueItem
from UI.ValuePicker import ValuePicker

T = TypeVar('T', bound=Union[datetime, int, str], covariant=True)


class MultiValuePicker(ValuePicker[T]):
    _options: List[MultiValueItem[T]]

    def __init__(self, message, options: List[MultiValueItem[T]]):
        super().__init__(message)
        if not options or len(options) == 0:
            print('The length of options must be greater than zero')
            exit()
        self._options = options

    def PickValue(self) -> T:
        print(self.inputMessage)
        for index, item in enumerate(self._options):
            print(f'{index+1} - {item.description}')
        return super().PickValue()

    def _ConvertValue(self, input: str) -> T:
        result = int(input)
        if result < 1 or result > len(self._options):
            print('The index must be between {0} and {1}'.format(
                1, len(self._options)))
            raise Exception()
        selectedOption = self._options[result-1]
        return selectedOption.id
