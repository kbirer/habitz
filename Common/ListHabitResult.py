from dataclasses import dataclass
from typing import List, Optional
from Common.ActionResult import ActionResult
from Common.Habit import Habit


@dataclass
class ListHabitResult(ActionResult):
    Habits: Optional[List[Habit]]

    def __init__(self, success: bool, errorMessage: Optional[str], habits: Optional[List[Habit]]) -> None:
        super().__init__(success, errorMessage)
        self.Habits = habits
