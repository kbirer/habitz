from dataclasses import dataclass

@dataclass
class HabitStreak():
    """Data class for habit streak information. 
        
    Attributes:
        
    HabitId -- Storage id of habit
    HabitName -- Description of habit
    StreakCount -- Number of streaks"""
    habit_id:int
    habit_name:str
    streak_count:int