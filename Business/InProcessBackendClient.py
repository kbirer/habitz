from datetime import datetime
import os
from typing import List, Optional
from Business.IBackendClient import IBackendClient
from Common.Config import Config
from Common.CheckedoutHabitResult import CheckedoutHabitResult
from Common.Habit import Habit
from Common.ListHabitResult import ListHabitResult
from Common.Periodicity import Periodicity
from Storage.IStorage import IStorage


class InProcessBackendClient(IBackendClient):
    _storage: IStorage

    def __init__(self, storage: IStorage):
        self._storage = storage

    def SaveHabit(self, name: str, periodicity: Periodicity, times: int, habitId: Optional[int]) -> None:
        try:
            if not habitId or habitId == 0:
                self._storage.AddHabit(name, periodicity, times)
            else:
                self._storage.UpdateHabit(habitId, name, periodicity, times)
        except BaseException as a:
            # todo log error here and hide it from user
            print(f'An error occured {a}')
            raise a

    def ListHabits(self) -> ListHabitResult:
        try:
            habits = self._storage.ListHabits()
            return ListHabitResult(True, None, habits)
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return ListHabitResult(False, 'An error occured', None)

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        try:
            # check that habit exists
            habit = self._storage.GetHabitById(habitId)
            if not habit:
                self._storage.CheckoutHabit(habitId, date)
            else:
                raise ValueError('habit not found')
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            raise e

    def ListCheckedoutHabits(self, startDate: datetime, endDate: datetime, pageIndex: int, pageSize: int) -> CheckedoutHabitResult:
        try:
            startDate = datetime(
                startDate.year, startDate.month, startDate.day, 0, 0, 0)
            endDate = datetime(endDate.year, endDate.month,
                               endDate.day, 23, 59, 59)
            checkedouts = self._storage.QueryCheckedoutHabits(
                startDate, endDate, pageIndex, pageSize)
            return CheckedoutHabitResult(True, None, checkedouts)
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return CheckedoutHabitResult(False, 'an error occured', None)

    def ClearAndSeedData(self):
        try:
            if Config().StorageType == 'csv':
                self.__DeleteFileIfExists(
                    Config().CsvCheckedOutHabitStorageFilePath)
                self.__DeleteFileIfExists(Config().CsvHabitStorageFilePath)
            elif Config().StorageType == 'sqlite':
                self.__DeleteFileIfExists(Config().SqliteDbPath)
            self._storage.ClearAndSeedTestData()
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            raise e

    def __DeleteFileIfExists(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)
