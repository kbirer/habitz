from datetime import datetime
from typing import Optional, Protocol
from Common.HabitStreakResult import HabitStreakResult
from Common.CheckedoutHabitResult import CheckedoutHabitResult
from Common.ListHabitResult import ListHabitResult
from Common.Periodicity import Periodicity
from Common.SelectHabitResult import SelectHabitResult


class IBackendClient(Protocol):
    """The protocol class for backend implementations"""
    def SaveHabit(self, name: str, periodicity: Periodicity, times: int, habitId: Optional[int]) -> None:
        pass

    def ListHabits(self) -> ListHabitResult:
        pass

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        pass

    def ListCheckedoutHabits(self, startDate: datetime, endDate: datetime) -> CheckedoutHabitResult:
        pass

    def ClearAndSeedData(self):
        pass

    def GetHabitById(self, id: int) -> SelectHabitResult:
        pass

    def GetAllLongestHabitStreaks(self) -> HabitStreakResult:
        pass

    def GetLongestHabitStreak(self, habitId: int) -> HabitStreakResult:
        pass
