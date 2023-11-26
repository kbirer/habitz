from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class CheckedOutHabit():
    """Data class for checked out habit information. 
        
    Attributes:
        
    HabitId -- Storage id of habit
    HabitDescription -- Description of habit
    CreationDate -- Checkout date of habit"""
    HabitId: int
    HabitDescription:Optional[str]
    CreationDate: datetime
