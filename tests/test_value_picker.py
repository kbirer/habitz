from io import StringIO
from unittest.mock import patch
import pytest
from pytest import raises
from ui.text_value_picker import TextValuePicker


@pytest.mark.parametrize('input_message', ['', None])
def test_value_picker_shoud_throw_exception_when_input_message_empty(
        input_message) -> None:
    with raises(Exception):
        assert ValuePicker(input_message)  # type: ignore


def test_value_picker_shoud_exit_program_if_exit_text_entered() -> None:
    with patch('sys.stdout', new=StringIO()):
        with patch('builtins.input', return_value="exit"):
            with raises(SystemExit):
                TextValuePicker('an input message').PickValue()  # type: ignore
