from io import BytesIO, TextIOWrapper
from unittest import mock
from storage.csv_file_storage import CsvFileStorage
from storage.sqlite_storage import SqliteStorage
from storage.storage_factory import StorageFactory


@mock.patch('configparser.open')
def test_Storage_Factory_Should_Return_Correct_Storage_For_Csv(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    storage = StorageFactory.create_storage()

    assert type(storage) == CsvFileStorage


@mock.patch('configparser.open')
def test_Storage_Factory_Should_Return_Correct_Storage_For_Sqlite(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = sqlite
    SqliteDbPath = Data/Data.sqlite
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    storage = StorageFactory.create_storage()

    assert type(storage) == SqliteStorage
