from dataclasses import dataclass

@dataclass
class HabitStreak():
    """Data class for habit streak information. 
        
    Attributes:
        
    HabitId -- Storage id of habit
    HabitName -- Description of habit
    StreakCount -- Number of streaks"""
    HabitId:int
    HabitName:str
    StreakCount:int