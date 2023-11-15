from datetime import datetime
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Habit import Habit
from Common.Periodicity import Periodicity


class TestData:
    TestHabits: list[Habit] = [
        Habit(1, 'Brush teeth', Periodicity.DAY, 2),
        Habit(2, 'Make a moderate workout', Periodicity.WEEK, 2),
        Habit(3, 'Wash car', Periodicity.MONTH, 1),
        Habit(4, 'Go to holiday', Periodicity.YEAR, 1),
        Habit(5, 'Go to shopping', Periodicity.WEEK, 1)
    ]

    TestCheckouts: list[CheckedOutHabit] = [
        CheckedOutHabit(HabitId= 1, HabitDescription= None, CreationDate= datetime(2023, 10, 10, 23, 10, 0)),
        CheckedOutHabit(HabitId= 1, HabitDescription= None, CreationDate= datetime(2023, 10, 10, 23, 10, 0)),
        CheckedOutHabit(HabitId= 1, HabitDescription= None, CreationDate= datetime(2023, 10, 11, 18, 10, 0)),
        CheckedOutHabit(HabitId= 1, HabitDescription= None, CreationDate= datetime(2023, 10, 11, 18, 10, 0)),
        CheckedOutHabit(HabitId= 1, HabitDescription= None, CreationDate= datetime(2023, 10, 12, 0, 10, 0)),
        CheckedOutHabit(HabitId= 1, HabitDescription= None, CreationDate= datetime(2023, 10, 12, 0, 10, 0)),
        CheckedOutHabit(HabitId= 2, HabitDescription= None, CreationDate= datetime(2023, 10, 5, 6, 10, 0)),
        CheckedOutHabit(HabitId= 3, HabitDescription= None, CreationDate= datetime(2023, 8, 5, 6, 10, 0)),
        CheckedOutHabit(HabitId= 4, HabitDescription= None, CreationDate= datetime(2023, 7, 1, 6, 10, 0)),
        CheckedOutHabit(HabitId= 4, HabitDescription= None, CreationDate= datetime(2024, 7, 2, 6, 10, 0)),
        CheckedOutHabit(HabitId= 4, HabitDescription= None, CreationDate= datetime(2025, 7, 2, 6, 10, 0)),
        CheckedOutHabit(HabitId= 5, HabitDescription= None, CreationDate= datetime(2023, 7, 3, 6, 10, 0)),
        CheckedOutHabit(HabitId= 5, HabitDescription= None, CreationDate= datetime(2023, 7, 9, 6, 10, 0)),
        CheckedOutHabit(HabitId= 5, HabitDescription= None, CreationDate= datetime(2023, 7, 12, 6, 10, 0)),
        CheckedOutHabit(HabitId= 5, HabitDescription= None, CreationDate= datetime(2023, 7, 15, 6, 10, 0))
    ]
