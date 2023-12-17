from dataclasses import dataclass
from typing import Optional
from common.action_result import ActionResult
from common.habit import Habit


@dataclass
class ListHabitResult(ActionResult):
    """Data class for listing habit results. Derives from ActionResult 

    Attributes:

    Habits -- List of habits"""
    habits: Optional[list[Habit]]

    def __init__(
            self, success: bool, error_message: Optional[str],
            habits: Optional[list[Habit]]) -> None:
        """Ctor

        Parameters:

        success -- Indicated backend operation is successful
        errorMessage -- Contains error message if backend operation is unsuccessfull
        habits -- List of habits"""
        super().__init__(success, error_message)
        self.habits = habits
