from dataclasses import dataclass
from typing import Optional
from Common.ActionResult import ActionResult
from Common.CheckedOutHabit import CheckedOutHabit

@dataclass
class CheckedoutHabitResult(ActionResult):
    """Data class for checked out habit information. Derives from ActionResult. 
        
    Attributes:

    CheckedoutHabits -- List of Checkedout habits"""
    CheckedoutHabits: Optional[list[CheckedOutHabit]]

    def __init__(self, success: bool, errorMessage: Optional[str], checkedoutHabits: Optional[list[CheckedOutHabit]]):
        """Constructor

        Parameters:

        success -- Indicated backend operation is successful
        errorMessage -- Contains error message if backend operation is unsuccessfull
        checkedoutHabits -- List of Checkedout habits"""
        super().__init__(success, errorMessage)
        self.CheckedoutHabits = checkedoutHabits
