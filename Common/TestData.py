from datetime import datetime
from typing import List
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Habit import Habit
from Common.Periodicity import Periodicity


class TestData:
    TestHabits: List[Habit] = [
        Habit(1, 'Brush teeth', Periodicity.DAY, 2),
        Habit(2, 'Make a moderate workout', Periodicity.WEEK, 2),
        Habit(3, 'Wash car', Periodicity.MONTH, 1),
        Habit(4, 'Go to holiday', Periodicity.YEAR, 1)
    ]

    TestCheckouts: List[CheckedOutHabit] = [
        CheckedOutHabit(1, datetime(2023, 10, 10, 23, 10, 0)),
        CheckedOutHabit(1, datetime(2023, 10, 10, 6, 10, 0)),
        CheckedOutHabit(2, datetime(2023, 10, 5, 6, 10, 0)),
        CheckedOutHabit(3, datetime(2023, 8, 5, 6, 10, 0)),
        CheckedOutHabit(4, datetime(2023, 7, 1, 6, 10, 0))
    ]
