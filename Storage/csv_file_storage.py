import csv
from datetime import datetime
import os
from typing import Optional
import pandas  # type: ignore
from common.checked_out_habit import CheckedOutHabit
from common.constants import Constants
from common.habit import Habit
from common.periodicity import Periodicity
from storage.istorage import IStorage
from common.test_data import TestData


class CsvFileStorage(IStorage):
    """Class for csv storage operations. Implements IStorage protocol class

    Attributes:

    _habitDefinitionsCsvFilePath -- habit definition csv file path
    _checkedOutHabitDefinitionsCsvFilePath -- checkedout habits csv file path"""
    _habit_definitions_csv_file_path: str
    _checked_out_habit_definitions_csv_file_path: str

    def __init__(self, habit_definitions_csv_file_path: str,
                 checkedout_habits_file_path: str):
        """Ctor

        Parameters:

        habitDefinitionsCsvFilePath -- habit definition csv file path
        checkedOutHabitsFilePath -- checkedout habits csv file path"""
        self._habit_definitions_csv_file_path = habit_definitions_csv_file_path
        self._checked_out_habit_definitions_csv_file_path = checkedout_habits_file_path

    def add_habit(self, description: str,
                  periodicity: Periodicity, times: int) -> int:
        """Function used to create new habit

        Parameters:

        description -- description of the habit
        periodicity -- period of the habit
        times -- Times that a habit must be checked out for a streak

        Returns:

        Storage id of the newly created habit"""
        lastId = 1
        with open(self._habit_definitions_csv_file_path, 'r', newline='') as csvFile:
            csvreader = csv.reader(csvFile)
            data = list(csvreader)
            if len(data) != 0:
                lastId = int(data[-1][0])+1
            csvFile.close()

        with open(self._habit_definitions_csv_file_path, 'a', newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            s = csvWriter.writerow(
                [lastId, description, periodicity.value, times])
            csvFile.close()
        return lastId

    def update_habit(self, id: int,
                     description: str, periodicity: Periodicity,
                     times: int) -> None:
        """Function used to update existing habit

        Parameters:

        id -- Storage id of the habit to update
        description -- description of the habit
        periodicity -- period of the habit
        times -- Times that a habit must be checked out for a streak"""
        df = pandas.read_csv(self._habit_definitions_csv_file_path,
                             header=None, index_col=0)
        df.at[id, Constants.HabitCsvFileColumnIndexes.name] = description
        df.at[id, Constants.HabitCsvFileColumnIndexes.periodicity] = periodicity.value
        df.at[id, Constants.HabitCsvFileColumnIndexes.times] = times
        df.to_csv(self._habit_definitions_csv_file_path,
                  header=None, index=True)

    def delete_habit(self, id: int) -> None:
        df = pandas.read_csv(
            self._habit_definitions_csv_file_path, header=None)
        df.drop(df.loc[df[Constants.HabitCsvFileColumnIndexes.id] == id])
        df.to_csv(self._habit_definitions_csv_file_path, index=False)

    def checkout_habit(self, habit_id: int, date: datetime) -> None:
        """Function used to delete existing habit

        Parameters:

        id -- Storage id of the habit to delete"""
        with open(self._checked_out_habit_definitions_csv_file_path, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([habit_id, date])
            csvFile.close()

    def list_habits(self) -> list[Habit]:
        """Function used to list all habits"""
        result = list[Habit]()
        with open(self._habit_definitions_csv_file_path, 'r', newline='') as csvFile:
            csvreader = csv.reader(csvFile)
            for row in csvreader:
                result.append(Habit(int(row[Constants.HabitCsvFileColumnIndexes.id]),
                                    row[Constants.HabitCsvFileColumnIndexes.name],
                                    Periodicity(
                                        int(row[Constants.HabitCsvFileColumnIndexes.periodicity])),
                                    int(row[Constants.HabitCsvFileColumnIndexes.times])))
            csvFile.close()
        return result

    def query_checkedout_habits(self, start: datetime,
                                end: datetime) -> list[CheckedOutHabit]:
        """Function used to query checkedout habits

        Parameters:

        start -- start date to query check out dates greater than
        end -- end date to query check out dates less than

        Returns:

        Checkedout habits for the given criteria"""
        result = list[CheckedOutHabit]()
        df = pandas.read_csv(
            self._checked_out_habit_definitions_csv_file_path, header=None)
        df[1] = pandas.to_datetime(df[1])
        df.set_index(1)
        query = df.sort_values(df.columns[0]).loc[df[1].between(start, end)]
        for _, row in query.iterrows():
            result.append(CheckedOutHabit(row[0], None, row[1]))
        return result

    def get_habit_by_id(self, habit_id: int) -> Optional[Habit]:
        """Function used to get habit by given storage id

        Parameters:

        habitId -- Storage id of habit to retrieve

        Returns:

        Habit with the given habit id or None if not found"""
        with open(self._habit_definitions_csv_file_path, 'r', newline='') as csvFile:
            csvreader = csv.reader(csvFile)
            for row in csvreader:
                if int(row[Constants.HabitCsvFileColumnIndexes.id]) == habit_id:
                    return Habit(int(row[Constants.HabitCsvFileColumnIndexes.id]),
                                 row[Constants.HabitCsvFileColumnIndexes.name],
                                 Periodicity(
                                     int(row[Constants.HabitCsvFileColumnIndexes.periodicity])),
                                 int(row[Constants.HabitCsvFileColumnIndexes.times]))
            csvFile.close()
            return None

    def clear_and_seed_test_data(self) -> None:
        """Function used to get habit by given storage id

        Parameters:

        habitId -- Storage id of habit to retrieve

        Returns:

        Habit with the given habit id or None if not found"""
        dirName = os.path.dirname(self._habit_definitions_csv_file_path)
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        dirName = os.path.dirname(
            self._checked_out_habit_definitions_csv_file_path)
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        with open(self._habit_definitions_csv_file_path, 'w', newline='') as csvFile:
            csvwriter = csv.writer(csvFile)
            for habit in TestData.test_habits:
                csvwriter.writerow(
                    [habit.id, habit.description, habit.periodicity.value, habit.times])
            csvFile.close()

        with open(self._checked_out_habit_definitions_csv_file_path, 'w', newline='') as csvFile:
            csvwriter = csv.writer(csvFile)
            for checkout in TestData.test_checkouts:
                csvwriter.writerow([checkout.habit_id, checkout.creation_date])
            csvFile.close()

    def get_habit_streaks(self, habitId: int,
                          periodicity: Periodicity, times: int) -> int:
        """Function used to get maximum streak of a habit

        Parameters:

        habitId -- Storage id of habit to retrieve streak information
        periodicity -- Periodicity of the habit
        times -- Times that the habit must be completed

        Returns:

        Maximum number of streaks of the given habit"""
        df = pandas.read_csv(
            self._checked_out_habit_definitions_csv_file_path, header=None)
        df[1] = pandas.to_datetime(df[1])
        match periodicity:
            case Periodicity.WEEK:
                df[2] = df[1].dt.isocalendar().week
            case Periodicity.YEAR:
                df[2] = df[1].dt.isocalendar().year
            case Periodicity.DAY:
                df[2] = df[1].dt.dayofyear
            case Periodicity.MONTH:
                df[2] = df[1].dt.month
        df.set_index([0], inplace=True, drop=False)
        filtered_df = df[df[0] == habitId]
        filtered_df = filtered_df.groupby(2).size().to_frame()
        filtered_df = filtered_df[filtered_df[0] >= times]
        filtered_df.drop(0, axis=1, inplace=True)
        filtered_df.reset_index(inplace=True)
        streaks = (filtered_df[2].diff() != 1).cumsum()
        result = streaks.map(streaks.value_counts())
        return result.max()  # type: ignore
