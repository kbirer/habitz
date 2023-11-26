
from dataclasses import dataclass
from typing import Optional

from Common.ActionResult import ActionResult
from Common.HabitStreak import HabitStreak


@dataclass
class HabitStreakResult(ActionResult):
    """Data class for habit streak results. Derives from ActionResult 
        
    Attributes:
        
    HabitStreaks -- List of habit streaks"""
    HabitStreaks: Optional[list[HabitStreak]]

    def __init__(self, success: bool, errorMessage: Optional[str]=None, habitStreaks: Optional[list[HabitStreak]]=None):
        """Ctor
            
        Parameters:
            
        success -- Indicated backend operation is successful
        errorMessage -- Contains error message if backend operation is unsuccessfull
        habitStreaks -- List of habit streaks"""
        super().__init__(success, errorMessage)
        self.HabitStreaks = habitStreaks
