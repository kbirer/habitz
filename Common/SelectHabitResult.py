from dataclasses import dataclass
from typing import Optional
from Common.ActionResult import ActionResult
from Common.Habit import Habit

@dataclass
class SelectHabitResult(ActionResult):
    """Data class for retrieving selected habit. Derives from ActionResult 
        
    Attributes:
        
    SelectedHabit -- Selected habit"""
    SelectedHabit:Optional[Habit]