import csv
from datetime import datetime
from typing import List, Optional
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Constants import Constants
from Common.Habit import Habit
from Common.Periodicity import Periodicity
from Storage.IStorage import IStorage
import pandas as pd  # type: ignore
from paginator import Paginator  # type: ignore
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
            list = list(csvreader)
            if len(list) != 0:
                lastId = int(list[-1][0])

        with open(self._habitDefinitionsCsvFilePath, 'w') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow([lastId, description, periodicity, times])
        return lastId

    def UpdateHabit(self, id: int, description: str, periodicity: Periodicity, times: int) -> None:
        df = pd.read_csv(self._habitDefinitionsCsvFilePath)
        rowToUpdate = df.loc[df[Constants.HabitCsvFileColumnIndexes.Id] == id]
        rowToUpdate[Constants.HabitCsvFileColumnIndexes.Name] = description
        rowToUpdate[Constants.HabitCsvFileColumnIndexes.Periodicity] = periodicity
        rowToUpdate[Constants.HabitCsvFileColumnIndexes.Times] = times
        df.to_csv(self._habitDefinitionsCsvFilePath, index=False)

    def DeleteHabit(self, id: int) -> None:
        df = pd.read_csv(self._habitDefinitionsCsvFilePath)
        df.drop(df.loc[df[Constants.HabitCsvFileColumnIndexes.Id] == id])
        df.to_csv(self._habitDefinitionsCsvFilePath, index=False)

    def CheckoutHabit(self, habitId: int, date: datetime) -> None:
        with open(self._checkedOutHabitDefinitionsCsvFilePath, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([habitId, date])

    def ListHabits(self) -> List[Habit]:
        result: List[Habit]
        with open(self._habitDefinitionsCsvFilePath, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            for row in csvreader:
                result.append(Habit(int(row[Constants.HabitCsvFileColumnIndexes.Id]),
                                    row[Constants.HabitCsvFileColumnIndexes.Name],
                                    Periodicity[row[Constants.HabitCsvFileColumnIndexes.Periodicity]],
                                    int(row[Constants.HabitCsvFileColumnIndexes.Times])))
        return result

    def QueryCheckedoutHabits(self, start: datetime, end: datetime, pageIndex: int, pageSize: int) -> List[CheckedOutHabit]:
        result: List[CheckedOutHabit]
        df = pd.read_csv(self._checkedOutHabitDefinitionsCsvFilePath)
        df[1] = pd.to_datetime(df[1])
        df.sort_values(by=df.columns[1], inplace=True)
        query = df.loc(df[df.columns[1]] <= end & df[df.columns[1]] >= start)
        paginator = Paginator(query, page=pageIndex, per_page=pageSize)
        # for page in paginator:
        # result.append(CheckedOutHabit(page.
        return result

    def GetHabitById(self, habitId: int) -> Optional[Habit]:
        with open(self._habitDefinitionsCsvFilePath, 'r') as csvFile:
            csvreader = csv.reader(csvFile)
            for row in csvreader:
                if int(row[Constants.HabitCsvFileColumnIndexes.Id]) == habitId:
                    return Habit(int(row[Constants.HabitCsvFileColumnIndexes.Id]),
                                 row[Constants.HabitCsvFileColumnIndexes.Name],
                                 Periodicity[row[Constants.HabitCsvFileColumnIndexes.Periodicity]],
                                 int(row[Constants.HabitCsvFileColumnIndexes.Times]))
            return None

    def ClearAndSeedTestData(self) -> None:
        with open(self._habitDefinitionsCsvFilePath, 'w') as csvFile:
            csvwriter = csv.writer(csvFile)
            for habit in TestData.TestHabits:
                csvwriter.writerow([habit.Id, habit.Description, habit.Periodicity, habit.Times])

        with open(self._checkedOutHabitDefinitionsCsvFilePath, 'w') as csvFile:
            csvwriter = csv.writer(csvFile)
            for checkout in TestData.TestCheckouts:
                csvwriter.writerow([checkout.HabitId, checkout.CreationDate])