import csv
from datetime import datetime
import os
from typing import Optional
import pandas  # type: ignore
from Common.CheckedOutHabit import CheckedOutHabit
from Common.Constants import Constants
from Common.Habit import Habit
from Common.Periodicity import Periodicity
from Storage.IStorage import IStorage
from Common.TestData import TestData


class CsvFileStorage(IStorage):
    """Class for csv storage operations. Implements IStorage protocol class
        
    Attributes:

    _habitDefinitionsCsvFilePath -- habit definition csv file path
    _checkedOutHabitDefinitionsCsvFilePath -- checkedout habits csv file path"""
    _habitDefinitionsCsvFilePath: str
    _checkedOutHabitDefinitionsCsvFilePath: str

    def __init__(self, habitDefinitionsCsvFilePath: str, checkedOutHabitsFilePath: str):
        """Ctor
            
        Parameters:

        habitDefinitionsCsvFilePath -- habit definition csv file path
        checkedOutHabitsFilePath -- checkedout habits csv file path"""
        self._habitDefinitionsCsvFilePath = habitDefinitionsCsvFilePath
        self._checkedOutHabitDefinitionsCsvFilePath = checkedOutHabitsFilePath

    def AddHabit(self, description: str, periodicity: Periodicity, times: int) -> int:
        """Function used to create new habit
            
        Parameters:

        description -- description of the habit
        periodicity -- period of the habit
        times -- Times that a habit must be checked out for a streak
        
        Returns:
        
        Storage id of the newly created habit"""
        lastId = 1
        with open(self._habitDefinitionsCsvFilePath, 'r', newline='') as csvFile:
            csvreader = csv.reader(csvFile)
            data = list(csvreader)
            if len(data) != 0:
                lastId = int(data[-1][0])+1
            csvFile.close()

        with open(self._habitDefinitionsCsvFilePath, 'a', newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            s = csvWriter.writerow(
                [lastId, description, periodicity.value, times])
            csvFile.close()
        return lastId

    def UpdateHabit(self, id: int, description: str, periodicity: Periodicity, times: int) -> None:
        """Function used to update existing habit
            
        Parameters:

        id -- Storage id of the habit to update
        description -- description of the habit
        periodicity -- period of the habit
        times -- Times that a habit must be checked out for a streak"""
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
        """Function used to delete existing habit
            
        Parameters:

        id -- Storage id of the habit to delete"""
        with open(self._checkedOutHabitDefinitionsCsvFilePath, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([habitId, date])
            csvFile.close()

    def ListHabits(self) -> list[Habit]:
        """Function used to list all habits"""
        result = list[Habit]()
        with open(self._habitDefinitionsCsvFilePath, 'r', newline='') as csvFile:
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
        """Function used to query checkedout habits
            
        Parameters:

        start -- start date to query check out dates greater than
        end -- end date to query check out dates less than
        
        Returns:
        
        Checkedout habits for the given criteria"""
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
        """Function used to get habit by given storage id
            
        Parameters:

        habitId -- Storage id of habit to retrieve
        
        Returns:
        
        Habit with the given habit id or None if not found"""
        with open(self._habitDefinitionsCsvFilePath, 'r', newline='') as csvFile:
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
        """Function used to get habit by given storage id
            
        Parameters:

        habitId -- Storage id of habit to retrieve
        
        Returns:
        
        Habit with the given habit id or None if not found"""
        dirName = os.path.dirname(self._habitDefinitionsCsvFilePath)
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        dirName = os.path.dirname(self._checkedOutHabitDefinitionsCsvFilePath)
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        with open(self._habitDefinitionsCsvFilePath, 'w', newline='') as csvFile:
            csvwriter = csv.writer(csvFile)
            for habit in TestData.TestHabits:
                csvwriter.writerow(
                    [habit.Id, habit.Description, habit.Periodicity.value, habit.Times])
            csvFile.close()

        with open(self._checkedOutHabitDefinitionsCsvFilePath, 'w', newline='') as csvFile:
            csvwriter = csv.writer(csvFile)
            for checkout in TestData.TestCheckouts:
                csvwriter.writerow([checkout.HabitId, checkout.CreationDate])
            csvFile.close()

    def GetHabitStreaks(self, habitId: int, periodicity: Periodicity, times: int) -> int:
        """Function used to get maximum streak of a habit
            
        Parameters:

        habitId -- Storage id of habit to retrieve streak information
        periodicity -- Periodicity of the habit
        times -- Times that the habit must be completed
        
        Returns:
        
        Maximum number of streaks of the given habit"""
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
