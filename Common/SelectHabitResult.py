from dataclasses import dataclass
from typing import Optional
from Common.ActionResult import ActionResult
from Common.Habit import Habit

@dataclass
class SelectHabitResult(ActionResult):
    SelectedHabit:Optional[Habit]