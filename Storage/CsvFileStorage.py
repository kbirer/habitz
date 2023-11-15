import csv
from datetime import datetime
import os
from typing import Optional
import pandas  # type: ignore
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Constants import Constants
from Common.Habit import Habit
from Common.HabitStreak import HabitStreak
from Common.Periodicity import Periodicity
from Storage.IStorage import IStorage
from pandas import DataFrame  # type: ignore
from Common.TestData import TestData


class CsvFileStorage(IStorage):

    _habitDefinitionsCsvFilePath: str
    _checkedOutHabitDefinitionsCsvFilePath: str

    def __init__(self, habitDefinitionsCsvFilePath: str, checkedOutHabitsFilePath: str):
        self._habitDefinitionsCsvFilePath = habitDefinitionsCsvFilePath
        self._checkedOutHabitDefinitionsCsvFilePath = checkedOutHabitsFilePath

    def AddHabit(self, description: str, periodicity: Periodicity, times: int) -> int:
        lastId = 1
        with open(self._habitDefinitionsCsvFilePath, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            data = list(csvreader)
            if len(data) != 0:
                lastId = int(data[-1][0])+1
            csvFile.close()

        with open(self._habitDefinitionsCsvFilePath, 'a') as csvFile:
            csvWriter = csv.writer(csvFile)
            s = csvWriter.writerow(
                [lastId, description, periodicity.value, times])
            csvFile.close()
        return lastId

    def UpdateHabit(self, id: int, description: str, periodicity: Periodicity, times: int) -> None:
        df = pandas.read_csv(self._habitDefinitionsCsvFilePath,
                             header=None, index_col=0)
        df.at[id, Constants.HabitCsvFileColumnIndexes.Name] = description
        df.at[id, Constants.HabitCsvFileColumnIndexes.Periodicity] = periodicity.value
        df.at[id, Constants.HabitCsvFileColumnIndexes.Times] = times
        df.to_csv(self._habitDefinitionsCsvFilePath, header=None, index=True)

    def DeleteHabit(self, id: int) -> None:
        df = pandas.read_csv(self._habitDefinitionsCsvFilePath, header=None)
        df.drop(df.loc[df[Constants.HabitCsvFileColumnIndexes.Id] == id])
        df.to_csv(self._habitDefinitionsCsvFilePath, index=False)

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        with open(self._checkedOutHabitDefinitionsCsvFilePath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([habitId, date])
            csvFile.close()

    def ListHabits(self) -> list[Habit]:
        result = list[Habit]()
        with open(self._habitDefinitionsCsvFilePath, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            for row in csvreader:
                result.append(Habit(int(row[Constants.HabitCsvFileColumnIndexes.Id]),
                                    row[Constants.HabitCsvFileColumnIndexes.Name],
                                    Periodicity(
                                        int(row[Constants.HabitCsvFileColumnIndexes.Periodicity])),
                                    int(row[Constants.HabitCsvFileColumnIndexes.Times])))
            csvFile.close()
        return result

    def QueryCheckedoutHabits(self, start: datetime, end: datetime) -> list[CheckedOutHabit]:
        result = list[CheckedOutHabit]()
        df = pandas.read_csv(
            self._checkedOutHabitDefinitionsCsvFilePath, header=None)
        df[1] = pandas.to_datetime(df[1])
        df.set_index(1)
        query = df.sort_values(df.columns[0]).loc[df[1].between(start, end)]
        for _, row in query.iterrows():
            result.append(CheckedOutHabit(row[0], None, row[1]))
        return result

    def GetHabitById(self, habitId: int) -> Optional[Habit]:
        with open(self._habitDefinitionsCsvFilePath, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            for row in csvreader:
                if int(row[Constants.HabitCsvFileColumnIndexes.Id]) == habitId:
                    return Habit(int(row[Constants.HabitCsvFileColumnIndexes.Id]),
                                 row[Constants.HabitCsvFileColumnIndexes.Name],
                                 Periodicity(
                                     int(row[Constants.HabitCsvFileColumnIndexes.Periodicity])),
                                 int(row[Constants.HabitCsvFileColumnIndexes.Times]))
            csvFile.close()
            return None

    def ClearAndSeedTestData(self) -> None:
        dirName = os.path.dirname(self._habitDefinitionsCsvFilePath)
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        dirName = os.path.dirname(self._checkedOutHabitDefinitionsCsvFilePath)
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        with open(self._habitDefinitionsCsvFilePath, 'w') as csvFile:
            csvwriter = csv.writer(csvFile)
            for habit in TestData.TestHabits:
                csvwriter.writerow(
                    [habit.Id, habit.Description, habit.Periodicity.value, habit.Times])
            csvFile.close()

        with open(self._checkedOutHabitDefinitionsCsvFilePath, 'w') as csvFile:
            csvwriter = csv.writer(csvFile)
            for checkout in TestData.TestCheckouts:
                csvwriter.writerow([checkout.HabitId, checkout.CreationDate])
            csvFile.close()

    def GetHabitStreaks(self, habitId: int, periodicity: Periodicity, times: int) -> int:
        df = pandas.read_csv(
            self._checkedOutHabitDefinitionsCsvFilePath, header=None)
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
        filteredDf = df[df[0] == habitId]
        filteredDf = filteredDf.groupby(2).size().to_frame()
        filteredDf = filteredDf[filteredDf[0] >= times]
        filteredDf.drop(0,axis=1,inplace=True)
        filteredDf.reset_index(inplace=True)
        streaks= (filteredDf[2].diff()!=1).cumsum()
        result=streaks.map(streaks.value_counts())
        return result.max()  # type: ignore
