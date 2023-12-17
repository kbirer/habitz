from datetime import datetime
from typing import Optional
from pandas import DataFrame  # type: ignore
from common.checked_out_habit import CheckedOutHabit
from common.habit import Habit
from common.habit_streak import HabitStreak
from common.periodicity import Periodicity
from storage.istorage import IStorage


class SqliteStorage(IStorage):
    """Class for sqlite storage operations. Implements IStorage protocol class.
    ToDo: must be implemented for sqlite storage support"""

    def __init__(self):
        pass

    def add_habit(self, description: str,
                  periodicity: Periodicity, times: int) -> int:
        return 0

    def update_habit(self, id: int,
                     description: str, periodicity: Periodicity,
                     times: int) -> None:
        pass

    def delete_habit(self, id: int) -> None:
        pass

    def checkout_habit(self, habitId: int,
                       date: datetime) -> None:
        pass

    def list_habits(self) -> list[Habit]:
        result: list[Habit]
        return result

    def query_checkedout_habits(self, start: datetime,
                                end: datetime) -> list[CheckedOutHabit]:
        result: list[CheckedOutHabit]
        return result

    def get_habit_by_id(self, habitId: int) -> Habit:
        raise BaseException()

    def clear_and_seed_test_data(self) -> None:
        pass

    def get_all_habit_streaks(self) -> Optional[list[HabitStreak]]:
        pass

    def get_habit_streaks(self, habitId: int,
                          periodicity: Periodicity, times: int) -> DataFrame:
        pass
