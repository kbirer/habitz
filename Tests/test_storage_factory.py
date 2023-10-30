from io import BytesIO, TextIOWrapper
from unittest import mock
from Common.Config import Config
from Storage.CsvFileStorage import CsvFileStorage
from Storage.SqliteStorage import SqliteStorage
from Storage.StorageFactory import StorageFactory


@mock.patch('configparser.open')
def test_Storage_Factory_Should_Return_Correct_Storage_For_Csv(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    storage = StorageFactory.CreateStorage()

    assert type(storage) == CsvFileStorage


@mock.patch('configparser.open')
def test_Storage_Factory_Should_Return_Correct_Storage_For_Sqlite(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = sqlite
    SqliteDbPath = Data/Data.sqlite
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    storage = StorageFactory.CreateStorage()

    assert type(storage) == SqliteStorage
