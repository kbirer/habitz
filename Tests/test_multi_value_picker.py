from typing import List
from unittest.mock import call, patch
from pytest import raises
import pytest
from UI.MultiValueItem import MultiValueItem
from UI.MultiValuePicker import MultiValuePicker


@pytest.mark.parametrize('options', [None, []])
def test_multi_value_picker_should_throw_exception_when_options_are_null_or_empty(options: List[MultiValueItem[int]]) -> None:
    with raises(SystemExit):
        MultiValuePicker[int]('please enter selection', options)


@patch('builtins.print')
def test_multi_value_picker_should_display_options_correctly(mockedPrint) -> None:
    options: List[MultiValueItem[str]] = [
        MultiValueItem[str]('1', '1st option'),
        MultiValueItem[str]('2', '2nd option')
    ]
    with patch('builtins.input', return_value="1"):
        picker = MultiValuePicker[str]('Please select', options)
        selected = picker.PickValue()
        for index,call in enumerate(mockedPrint.call_args_list):
            args, _ = call
            match(index):
                case 0:
                    assert args[0]=='Please select'
                case 1:
                    assert args[0]=='1 - 1st option'
                case 2:
                    assert args[0]=='2 - 2nd option'
        assert selected == '1'
