from datetime import datetime
import os
from typing import Optional
from business.ibackend_client import IBackendClient
from common.config import Config
from common.checkedout_habit_result import CheckedoutHabitResult
from common.habit_streak import HabitStreak
from common.habit_streak_result import HabitStreakResult
from common.list_habit_result import ListHabitResult
from common.periodicity import Periodicity
from common.select_habit_result import SelectHabitResult
from storage.istorage import IStorage


class InProcessBackendClient(IBackendClient):
    """The backend implementation which runs inside the same process with UI. Implements IBackendClient protocol class"""
    _storage: IStorage

    def __init__(self, storage: IStorage):
        """Constructor

        Parameters:

        storage -- Storage implementation to use"""
        self._storage = storage

    def save_habit(self, name: str,
                  periodicity: Periodicity, times: int,
                  habit_id: Optional[int]) -> None:
        """Backend function to create or update new habit.

        Parameters:

        name -- Name of the habit.
        periodicity -- Peridicity of the habit
        times -- How many times this habit must be completed in given periodicity to achieve a streak
        habitId -- Storage id of the habit, optional. Zero or none to create a new habit, an integer to update the habit with specified integer"""
        try:
            if not habit_id or habit_id == 0:
                self._storage.add_habit(name, periodicity, times)
            else:
                self._storage.update_habit(habit_id, name, periodicity, times)
        except BaseException as a:
            # todo log error here and hide it from user
            print(f'An error occured {a}')
            raise a

    def list_habits(self) -> ListHabitResult:
        """Backend function to list habits.

        Returns:

        A new instance of ListHabitResult which contains habits to list"""
        try:
            habits = self._storage.list_habits()
            return ListHabitResult(True, None, habits)
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return ListHabitResult(False, 'An error occured', None)

    def checkout_habit(self, habit_id: int,
                      date: datetime) -> None:
        """Backend function to checkout a new habit.

        Parameters:

        habitId -- Storage id of habit.
        date -- Checkout date of the habit"""
        try:
            # check that habit exists
            habit = self._storage.get_habit_by_id(habit_id)
            if habit:
                self._storage.checkout_habit(habit_id, date)
            else:
                raise ValueError('habit not found')
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            raise e

    def list_checkedout_habits(self, start_date: datetime,
                               end_date: datetime) -> CheckedoutHabitResult:
        """Backend function to list checkedout habits. 

        Parameters:
        startDate -- Start date which checkout dates must be greater.
        endDate -- End date which checkout dates must be lesser.

        Returns:

        A new instance of CheckedoutHabitResult which contains checkedout habits"""
        try:
            start_date = datetime(
                start_date.year, start_date.month, start_date.day, 0, 0, 0)
            end_date = datetime(end_date.year, end_date.month,
                               end_date.day, 23, 59, 59)
            checkedouts = self._storage.query_checkedout_habits(
                start_date, end_date)
            list_habit_result = self.list_habits()
            if list_habit_result.success:
                habit_dictionary: dict = {}
                for habit in list_habit_result.habits:  # type: ignore
                    habit_dictionary[habit.id] = habit.description
                for checkedout_habit in checkedouts:
                    checkedout_habit.habit_description = habit_dictionary[checkedout_habit.habit_id]
            else:
                return CheckedoutHabitResult(
                    True, list_habit_result.error_message, None)
            return CheckedoutHabitResult(True, None, checkedouts)
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return CheckedoutHabitResult(False, 'an error occured', None)

    def clear_and_seed_data(self):
        """Backend function to clear and create a new test data"""
        try:
            if Config().storage_type == 'csv':
                self.__delete_file_if_exists(
                    Config().csv_checked_out_habit_storage_file_path)
                self.__delete_file_if_exists(Config().csv_habit_storage_file_path)
            elif Config().storage_type == 'sqlite':
                self.__delete_file_if_exists(Config().sqlite_db_path)
            self._storage.clear_and_seed_test_data()
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            raise e

    def get_habit_by_id(self, id: int) -> SelectHabitResult:
        """Backend function to get information about habit. 

        Parameters:

        id -- Storage id of habit to fetch for information

        Returns:

        A new instance of SelectHabitResult which contains selected habit data"""
        try:
            habit = self._storage.get_habit_by_id(id)
            return SelectHabitResult(True, '', habit)
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return SelectHabitResult(False, 'Error', None)

    def get_all_longest_habit_streaks(self) -> HabitStreakResult:
        """Backend function to get longest habit streaks."""
        try:
            result: HabitStreakResult = HabitStreakResult(
                True, habit_streaks=[])
            habits = self._storage.list_habits()
            for habit in habits:
                max_streak = self._storage.get_habit_streaks(
                    habit.id, habit.periodicity, habit.times)
                result.habit_streaks.append(
                    HabitStreak(
                        habit.id, habit.description,
                        max_streak))  # type: ignore
            return result
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return HabitStreakResult(success=False)

    def get_longest_habit_streak(self, habit_id: int) -> HabitStreakResult:
        """Backend function to get longest streak of a single habit.

        Parameters:

        habitId -- Storage id of habit to fetch for streak information"""
        try:
            result: HabitStreakResult = HabitStreakResult(
                True, habit_streaks=[])
            habit = self._storage.get_habit_by_id(habit_id)
            if not habit:
                return HabitStreakResult(False, 'Habit not found')
            max_streak = self._storage.get_habit_streaks(
                habit_id, habit.periodicity, habit.times)
            result.habit_streaks.append(
                HabitStreak(
                    habit.id, habit.description,
                    max_streak))  # type: ignore
            return result
        except BaseException as e:
            # todo log error here and hide it from user
            print(f'An error occured {e}')
            return HabitStreakResult(success=False)

    def __delete_file_if_exists(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)
