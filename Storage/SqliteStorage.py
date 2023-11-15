from datetime import datetime
from typing import Optional
from pandas import DataFrame # type: ignore
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Habit import Habit
from Common.HabitStreak import HabitStreak
from Common.Periodicity import Periodicity
from Storage.IStorage import IStorage
from Storage.IStorage import IStorage


class SqliteStorage(IStorage):
    def __init__(self):
        pass

    def AddHabit(self, description: str, periodicity: Periodicity, times: int) -> int:
        return 0

    def UpdateHabit(self, id: int, description: str, periodicity: Periodicity, times: int) -> None:
        pass

    def DeleteHabit(self, id: int) -> None:
        pass

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        pass

    def ListHabits(self) -> list[Habit]:
        result: list[Habit]
        return result

    def QueryCheckedoutHabits(self, start: datetime, end: datetime) -> list[CheckedOutHabit]:
        result: list[CheckedOutHabit]
        return result
    
    def GetHabitById(self, habitId: int) -> Habit:
        raise BaseException()
    
    def ClearAndSeedTestData(self) -> None:
        pass
    
    def GetAllHabitStreaks(self) -> Optional[list[HabitStreak]]:
        pass

    def GetHabitStreaks(self, habitId: int,periodicity:Periodicity,times:int) -> DataFrame:
        pass