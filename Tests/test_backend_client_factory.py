from io import BytesIO, TextIOWrapper
from unittest import mock
from Business.BackendClientFactory import BackendClientFactory
from Business.InProcessBackendClient import InProcessBackendClient
from Common.Config import Config
from Storage.CsvFileStorage import CsvFileStorage
from Storage.SqliteStorage import SqliteStorage
from Storage.StorageFactory import StorageFactory


@mock.patch('configparser.open')
def test_BackendClient_Factory_Should_Return_Correct_ClientType(mockFileOpen: mock.MagicMock):
    mockFileOpen.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    client = BackendClientFactory.CreateBackendClient()

    assert type(client) == InProcessBackendClient

