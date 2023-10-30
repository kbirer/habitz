from datetime import datetime
from typing import List
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Habit import Habit
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

    def ListHabits(self) -> List[Habit]:
        result: List[Habit]
        return result

    def QueryCheckedoutHabits(self, start: datetime, end: datetime, pageIndex: int, pageSize: int) -> List[CheckedOutHabit]:
        result: List[CheckedOutHabit]
        return result
    
    def GetHabitById(self, habitId: int) -> Habit:
        raise BaseException()
    
    def ClearAndSeedTestData(self) -> None:
        pass