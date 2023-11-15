from datetime import datetime
import os
from typing import Optional
from Business.IBackendClient import IBackendClient
from Common.Config import Config
from Common.CheckedoutHabitResult import CheckedoutHabitResult
from Common.Habit import Habit
from Common.HabitStreak import HabitStreak
from Common.HabitStreakResult import HabitStreakResult
from Common.ListHabitResult import ListHabitResult
from Common.Periodicity import Periodicity
from Common.SelectHabitResult import SelectHabitResult
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
            if habit:
                self._storage.CheckoutHabit(habitId, date)
            else:
                raise ValueError('habit not found')
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            raise e

    def ListCheckedoutHabits(self, startDate: datetime, endDate: datetime) -> CheckedoutHabitResult:
        try:
            startDate = datetime(startDate.year, startDate.month, startDate.day, 0, 0, 0)
            endDate = datetime(endDate.year, endDate.month,endDate.day, 23, 59, 59)
            checkedouts = self._storage.QueryCheckedoutHabits(startDate, endDate)
            listHabitResult=self.ListHabits()
            if listHabitResult.Success:
                habitDictionary:dict={}
                for habit in listHabitResult.Habits:  # type: ignore
                    habitDictionary[habit.Id] = habit.Description
                for checkedoutHabit in checkedouts:
                    checkedoutHabit.HabitDescription=habitDictionary[checkedoutHabit.HabitId]
            else:
                return CheckedoutHabitResult(True, listHabitResult.ErrorMessage, None)
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

    def GetHabitById(self, id: int) -> SelectHabitResult:
        try:
            habit = self._storage.GetHabitById(id)
            return SelectHabitResult(True, '', habit)
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return SelectHabitResult(False, 'Error', None)

    def GetAllLongestHabitStreaks(self) -> HabitStreakResult:
        try:
            result:HabitStreakResult=HabitStreakResult(True,habitStreaks=[])
            habits = self._storage.ListHabits()
            for habit in habits:
                maxStreak = self._storage.GetHabitStreaks(habit.Id,habit.Periodicity,habit.Times)
                result.HabitStreaks.append(HabitStreak(habit.Id,habit.Description,maxStreak))# type: ignore
            return result
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return HabitStreakResult(success=False)
        
    def GetLongestHabitStreak(self, habitId: int) -> HabitStreakResult:
        try:
            result:HabitStreakResult=HabitStreakResult(True,habitStreaks=[])
            habit = self._storage.GetHabitById(habitId)
            if not habit:
                return HabitStreakResult(False,'Habit not found')
            maxStreak = self._storage.GetHabitStreaks(habitId,habit.Periodicity,habit.Times)
            result.HabitStreaks.append(HabitStreak(habit.Id,habit.Description,maxStreak))# type: ignore
            return result
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return HabitStreakResult(success=False)
        
    def __DeleteFileIfExists(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)
