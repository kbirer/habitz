from datetime import datetime
from common.checked_out_habit import CheckedOutHabit
from common.habit import Habit
from common.periodicity import Periodicity


class TestData:
    """Class contains predefined test data 
        
    Attributes:

    TestHabits -- Predefined habits
    TestCheckouts -- Predefined checked out habits"""
    test_habits: list[Habit] = [
        Habit(1, 'Brush teeth', Periodicity.DAY, 2),
        Habit(2, 'Make a moderate workout', Periodicity.WEEK, 2),
        Habit(3, 'Wash car', Periodicity.MONTH, 1),
        Habit(4, 'Go to holiday', Periodicity.YEAR, 1),
        Habit(5, 'Go to shopping', Periodicity.WEEK, 1)
    ]

    test_checkouts: list[CheckedOutHabit] = [
        CheckedOutHabit(habit_id= 1, habit_description= None, creation_date= datetime(2023, 10, 10, 23, 10, 0)),
        CheckedOutHabit(habit_id= 1, habit_description= None, creation_date= datetime(2023, 10, 10, 23, 10, 0)),
        CheckedOutHabit(habit_id= 1, habit_description= None, creation_date= datetime(2023, 10, 11, 18, 10, 0)),
        CheckedOutHabit(habit_id= 1, habit_description= None, creation_date= datetime(2023, 10, 11, 18, 10, 0)),
        CheckedOutHabit(habit_id= 1, habit_description= None, creation_date= datetime(2023, 10, 12, 0, 10, 0)),
        CheckedOutHabit(habit_id= 1, habit_description= None, creation_date= datetime(2023, 10, 12, 0, 10, 0)),
        CheckedOutHabit(habit_id= 2, habit_description= None, creation_date= datetime(2023, 10, 5, 6, 10, 0)),
        CheckedOutHabit(habit_id= 3, habit_description= None, creation_date= datetime(2023, 8, 5, 6, 10, 0)),
        CheckedOutHabit(habit_id= 4, habit_description= None, creation_date= datetime(2023, 7, 1, 6, 10, 0)),
        CheckedOutHabit(habit_id= 4, habit_description= None, creation_date= datetime(2024, 7, 2, 6, 10, 0)),
        CheckedOutHabit(habit_id= 4, habit_description= None, creation_date= datetime(2025, 7, 2, 6, 10, 0)),
        CheckedOutHabit(habit_id= 5, habit_description= None, creation_date= datetime(2023, 7, 3, 6, 10, 0)),
        CheckedOutHabit(habit_id= 5, habit_description= None, creation_date= datetime(2023, 7, 9, 6, 10, 0)),
        CheckedOutHabit(habit_id= 5, habit_description= None, creation_date= datetime(2023, 7, 12, 6, 10, 0)),
        CheckedOutHabit(habit_id= 5, habit_description= None, creation_date= datetime(2023, 7, 15, 6, 10, 0))
    ]
