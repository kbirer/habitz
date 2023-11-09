from datetime import datetime
from typing import Optional, Protocol
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Habit import Habit
from Common.Periodicity import Periodicity


class IStorage(Protocol):

    def AddHabit(self, description: str, periodicity: Periodicity, times: int) -> int:
        pass

    def UpdateHabit(self, id: int, description: str, periodicity: Periodicity, times: int) -> None:
        pass

    def DeleteHabit(self, id: int) -> None:
        pass

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        pass

    def ListHabits(self) -> list[Habit]:
        pass

    def QueryCheckedoutHabits(self, start: datetime, end: datetime) -> list[CheckedOutHabit]:
        pass

    def ClearAndSeedTestData(self) -> None:
        pass

    def GetHabitById(self, habitId: int) -> Optional[Habit]:
        pass
