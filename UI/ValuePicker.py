from abc import abstractmethod
from datetime import datetime
from typing import Protocol, TypeVar, Union
from UI.UIHelper import UIHelper

T = TypeVar('T', bound=Union[datetime, int, str], covariant=True)

class ValuePicker(Protocol[T]):
    inputMessage: str

    def __init__(self, inputMessage: str):
        if not inputMessage:
            raise Exception(
                'inputMessage parameter can\'t be none or empty string')
        self.inputMessage = inputMessage

    def PickValue(self) -> T:
        while True:
            try:
                result = input(self.inputMessage+"\n")
                if not result:
                    continue
                UIHelper.ExitIfCommanded(result)
                return self._ConvertValue(result)
            except Exception as e:
                print(e)
    
    @abstractmethod
    def _ConvertValue(self, input: str) -> T:
        pass
