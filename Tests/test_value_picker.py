from io import StringIO
from unittest.mock import patch
import pytest
from pytest import raises
from UI.TextValuePicker import TextValuePicker


@pytest.mark.parametrize('inputMessage', ['', None])
def test_value_picker_shoud_throw_exception_when_input_message_empty(inputMessage) -> None:
    with raises(Exception):
        assert ValuePicker(inputMessage)  # type: ignore

def test_value_picker_shoud_exit_program_if_exit_text_entered() -> None:
    with patch('sys.stdout', new=StringIO()):
        with patch('builtins.input', return_value="exit"):
            with raises(SystemExit):
                TextValuePicker('an input message').PickValue()  # type: ignore
