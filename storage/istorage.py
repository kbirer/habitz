from datetime import datetime
from typing import Optional, Protocol
from common.checked_out_habit import CheckedOutHabit
from common.habit import Habit
from common.periodicity import Periodicity


class IStorage(Protocol):
    """Protocol class for storage operations"""

    def add_habit(self, description: str,
                  periodicity: Periodicity, times: int) -> int:
        pass

    def update_habit(self, id: int,
                     description: str, periodicity: Periodicity,
                     times: int) -> None:
        pass

    def delete_habit(self, id: int) -> None:
        pass

    def checkout_habit(self, habit_id: int,
                       date: datetime) -> None:
        pass

    def list_habits(self) -> list[Habit]:
        pass

    def query_checkedout_habits(self, start: datetime,
                                end: datetime) -> list[CheckedOutHabit]:
        pass

    def clear_and_seed_test_data(self) -> None:
        pass

    def get_habit_by_id(self, habit_id: int) -> Optional[Habit]:
        pass

    def get_habit_streaks(self, habit_id: int,
                          periodicity: Periodicity, times: int) -> int:
        pass
