from dataclasses import dataclass
from typing import Optional
from common.action_result import ActionResult
from common.checked_out_habit import CheckedOutHabit

@dataclass
class CheckedoutHabitResult(ActionResult):
    """Data class for checked out habit information. Derives from ActionResult. 
        
    Attributes:

    CheckedoutHabits -- List of Checkedout habits"""
    checkedout_habits: Optional[list[CheckedOutHabit]]

    def __init__(self, success: bool, 
                 error_message: Optional[str], checkedout_habits: Optional[list[CheckedOutHabit]]):
        """Constructor

        Parameters:

        success -- Indicated backend operation is successful
        errorMessage -- Contains error message if backend operation is unsuccessfull
        checkedoutHabits -- List of Checkedout habits"""
        super().__init__(success, error_message)
        self.checkedout_habits = checkedout_habits
