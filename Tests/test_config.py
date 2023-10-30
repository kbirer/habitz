from io import BytesIO, TextIOWrapper
from unittest import mock
from pytest import raises
import pytest
from Common.Config import Config


@mock.patch('configparser.open')
def test_Configuration_File_Should_Work_Correctly_For_Csv(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    assert Config().CsvHabitStorageFilePath == 'Data/HabitDefinitions.csv'
    assert Config().CsvCheckedOutHabitStorageFilePath == 'Data/CheckedoutHabits.csv'
    assert not Config().ClearAndSeedData
    assert not Config().SqliteDbPath
    assert Config().ClientType == 'InProcess'


@mock.patch('configparser.open')
def test_Storage_Type_Should_Be_Either_Csv_Or_Sqlite(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = other
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    with raises(ValueError):
        Config()


@mock.patch('configparser.open')
def test_For_Csv_Storage_Type_Habit_Storage_Paths_Should_Exists(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    with raises(ValueError) as error:
        Config()
    assert "CsvHabitStorageFilePath" in str(error.value)


@mock.patch('configparser.open')
def test_For_Csv_Storage_Type_Checkedout_Habit_Storage_Paths_Should_Exists(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    with raises(ValueError) as error:
        Config()
    assert "CsvCheckedOutHabitStorageFilePath" in str(error.value)

@mock.patch('configparser.open')
@pytest.mark.parametrize('clientType', ['', 'WebService'])
def test_Backend_client_type_should_be_not_empty_and_inprocess(mockFileOpen: mock.MagicMock,clientType:str):
    mockedConfig=f"[DATA_STORAGE]\n StorageType = csv\n CsvHabitStorageFilePath = Data/HabitDefinitions.csv\n CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv\n [BACKEND_CLIENT] ClientType = {clientType}".encode('utf-8')
    mockFileOpen.return_value = TextIOWrapper(BytesIO(mockedConfig))

    with raises(ValueError) as error:
        Config()
    assert "InProcess" in str(error.value)