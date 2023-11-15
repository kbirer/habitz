
from dataclasses import dataclass
from typing import Optional

from Common.ActionResult import ActionResult
from Common.HabitStreak import HabitStreak


@dataclass
class HabitStreakResult(ActionResult):
    HabitStreaks: Optional[list[HabitStreak]]

    def __init__(self, success: bool, errorMessage: Optional[str]=None, habitStreaks: Optional[list[HabitStreak]]=None):
        super().__init__(success, errorMessage)
        self.HabitStreaks = habitStreaks
