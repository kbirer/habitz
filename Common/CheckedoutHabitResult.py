from dataclasses import dataclass
from typing import Optional
from Common.ActionResult import ActionResult
from Common.CheckedOutHabit import CheckedOutHabit

@dataclass
class CheckedoutHabitResult(ActionResult):
    CheckedoutHabits: Optional[list[CheckedOutHabit]]

    def __init__(self, success: bool, errorMessage: Optional[str], checkedoutHabits: Optional[list[CheckedOutHabit]]):
        super().__init__(success, errorMessage)
        self.CheckedoutHabits = checkedoutHabits
