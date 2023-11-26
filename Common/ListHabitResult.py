from dataclasses import dataclass
from typing import Optional
from Common.ActionResult import ActionResult
from Common.Habit import Habit


@dataclass
class ListHabitResult(ActionResult):
    """Data class for listing habit results. Derives from ActionResult 
        
    Attributes:
        
    Habits -- List of habits"""
    Habits: Optional[list[Habit]]

    def __init__(self, success: bool, errorMessage: Optional[str], habits: Optional[list[Habit]]) -> None:
        """Ctor
            
        Parameters:
            
        success -- Indicated backend operation is successful
        errorMessage -- Contains error message if backend operation is unsuccessfull
        habits -- List of habits"""
        super().__init__(success, errorMessage)
        self.Habits = habits
