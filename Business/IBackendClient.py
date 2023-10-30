from datetime import datetime
from typing import List, Optional, Protocol
from Common.CheckedoutHabitResult import CheckedoutHabitResult
from Common.ListHabitResult import ListHabitResult
from Common.Periodicity import Periodicity


class IBackendClient(Protocol):
    def SaveHabit(self, name: str, periodicity: Periodicity, times: int, habitId: Optional[int]) -> None:
        pass

    def ListHabits(self) -> ListHabitResult:
        pass

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        pass

    def ListCheckedoutHabits(self, startDate: datetime, endDate: datetime, pageIndex: int, pageSize: int) -> CheckedoutHabitResult:
        pass

    def ClearAndSeedData(self):
        pass
