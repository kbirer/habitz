from dataclasses import dataclass
from typing import Optional
from Common.ActionResult import ActionResult
from Common.Habit import Habit


@dataclass
class ListHabitResult(ActionResult):
    Habits: Optional[list[Habit]]

    def __init__(self, success: bool, errorMessage: Optional[str], habits: Optional[list[Habit]]) -> None:
        super().__init__(success, errorMessage)
        self.Habits = habits
