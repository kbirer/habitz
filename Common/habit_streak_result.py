from dataclasses import dataclass
from typing import Optional
from common.action_result import ActionResult
from common.habit_streak import HabitStreak


@dataclass
class HabitStreakResult(ActionResult):
    """Data class for habit streak results. Derives from ActionResult 

    Attributes:

    HabitStreaks -- List of habit streaks"""
    habit_streaks: Optional[list[HabitStreak]]

    def __init__(
            self, success: bool, error_message: Optional[str] = None,
            habit_streaks: Optional[list[HabitStreak]] = None):
        """Ctor

        Parameters:

        success -- Indicated backend operation is successful
        errorMessage -- Contains error message if backend operation is unsuccessfull
        habitStreaks -- List of habit streaks"""
        super().__init__(success, error_message)
        self.habit_streaks = habit_streaks
