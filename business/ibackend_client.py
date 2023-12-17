from datetime import datetime
from typing import Optional, Protocol
from common.habit_streak_result import HabitStreakResult
from common.checkedout_habit_result import CheckedoutHabitResult
from common.list_habit_result import ListHabitResult
from common.periodicity import Periodicity
from common.select_habit_result import SelectHabitResult


class IBackendClient(Protocol):
    """The protocol class for backend implementations"""

    def save_habit(self, name: str,
                   periodicity: Periodicity, times: int,
                   habit_id: Optional[int]) -> None:
        pass

    def list_habits(self) -> ListHabitResult:
        pass

    def checkout_habit(self, habit_id: int, 
                       date: datetime) -> None:
        pass

    def list_checkedout_habits(self, start_date: datetime,
                               end_date: datetime) -> CheckedoutHabitResult:
        pass

    def clear_and_seed_data(self):
        pass

    def get_habit_by_id(self, id: int) -> SelectHabitResult:
        pass

    def get_all_longest_habit_streaks(self) -> HabitStreakResult:
        pass

    def get_longest_habit_streak(self, habit_id: int) -> HabitStreakResult:
        pass
