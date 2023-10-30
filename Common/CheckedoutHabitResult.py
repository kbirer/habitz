from typing import List, Optional
from Common.ActionResult import ActionResult
from Common.CheckedOutHabit import CheckedOutHabit


class CheckedoutHabitResult(ActionResult):
    CheckedoutHabits: Optional[List[CheckedOutHabit]]

    def __init__(self, success: bool, errorMessage: Optional[str], checkedoutHabits: Optional[List[CheckedOutHabit]]):
        super().__init__(success, errorMessage)
        self.CheckedoutHabits = checkedoutHabits
