from io import BytesIO, TextIOWrapper
from unittest import mock
from pytest import raises
import pytest
from common.config import Config


@mock.patch('configparser.open')
def test_Configuration_File_Should_Work_Correctly_For_Csv(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    assert Config().csv_habit_storage_file_path == 'Data/HabitDefinitions.csv'
    assert Config().csv_checked_out_habit_storage_file_path == 'Data/CheckedoutHabits.csv'
    assert not Config().clear_and_seed_data
    assert not Config().sqlite_db_path
    assert Config().client_type == 'InProcess'


@mock.patch('configparser.open')
def test_Storage_Type_Should_Be_Either_Csv_Or_Sqlite(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = other
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    with raises(ValueError):
        Config()


@mock.patch('configparser.open')
def test_For_Csv_Storage_Type_Habit_Storage_Paths_Should_Exists(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    with raises(ValueError) as error:
        Config()
    assert "CsvHabitStorageFilePath" in str(error.value)


@mock.patch('configparser.open')
def test_For_Csv_Storage_Type_Checkedout_Habit_Storage_Paths_Should_Exists(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    with raises(ValueError) as error:
        Config()
    assert "CsvCheckedOutHabitStorageFilePath" in str(error.value)


@mock.patch('configparser.open')
@pytest.mark.parametrize('client_type', ['', 'WebService'])
def test_Backend_client_type_should_be_not_empty_and_inprocess(
        mock_file_open: mock.MagicMock, client_type: str):
    mockedConfig = f"[DATA_STORAGE]\n StorageType = csv\n CsvHabitStorageFilePath = Data/HabitDefinitions.csv\n CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv\n [BACKEND_CLIENT] ClientType = {
        client_type}".encode('utf-8')
    mock_file_open.return_value = TextIOWrapper(BytesIO(mockedConfig))

    with raises(ValueError) as error:
        Config()
    assert "InProcess" in str(error.value)
