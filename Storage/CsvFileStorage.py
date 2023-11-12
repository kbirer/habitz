import csv
from datetime import datetime
from typing import List, Optional
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Constants import Constants
from Common.Habit import Habit
from Common.Periodicity import Periodicity
from Storage.IStorage import IStorage
import pandas as pd  # type: ignore
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
        df = pd.read_csv(self._habitDefinitionsCsvFilePath,
                         header=None, index_col=0)
        df.at[id, Constants.HabitCsvFileColumnIndexes.Name] = description
        df.at[id, Constants.HabitCsvFileColumnIndexes.Periodicity] = periodicity.value
        df.at[id, Constants.HabitCsvFileColumnIndexes.Times] = times
        df.to_csv(self._habitDefinitionsCsvFilePath, header=None, index=True)

    def DeleteHabit(self, id: int) -> None:
        df = pd.read_csv(self._habitDefinitionsCsvFilePath, header=None)
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
        df = pd.read_csv(self._checkedOutHabitDefinitionsCsvFilePath, header=None)
        df[1] = pd.to_datetime(df[1])
        query = df[df[1].between(start, end)]
        for item in query.iterrows():
            result.append(CheckedOutHabit(item[0],None,item[1]))
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
