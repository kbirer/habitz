from dataclasses import dataclass
from typing import Optional
from common.action_result import ActionResult
from common.habit import Habit


@dataclass
class SelectHabitResult(ActionResult):
    """Data class for retrieving selected habit. Derives from ActionResult 

    Attributes:

    SelectedHabit -- Selected habit"""
    selected_habit: Optional[Habit]
