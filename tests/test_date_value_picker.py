from datetime import datetime
from io import StringIO
from unittest.mock import patch
from common.constants import Constants
from ui.date_value_picker import DateValuePicker


def test_date_value_picker_shoud_work_correctly() -> None:
    with patch('sys.stdout', new=StringIO()):
        with patch('builtins.input', return_value="10/10/2023"):
            picker = DateValuePicker(
                'Please enter date', Constants.date_picker_format)
            result = picker.PickValue()
            assert type(result) == datetime
            assert result.day == result.month == 10
            assert result.year == 2023
