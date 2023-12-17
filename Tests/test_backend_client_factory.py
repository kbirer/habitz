from io import BytesIO, TextIOWrapper
from unittest import mock
from business.backend_client_factory import BackendClientFactory
from business.in_process_backend_client import InProcessBackendClient


@mock.patch('configparser.open')
def test_BackendClient_Factory_Should_Return_Correct_ClientType(
        mock_file_open: mock.MagicMock):
    mock_file_open.return_value = TextIOWrapper(BytesIO(b"""[DATA_STORAGE]
    StorageType = csv
    CsvHabitStorageFilePath = Data/HabitDefinitions.csv
    CsvCheckedOutHabitStorageFilePath = Data/CheckedoutHabits.csv
    [BACKEND_CLIENT]
    ClientType = InProcess"""))

    client = BackendClientFactory.create_backend_client()

    assert type(client) == InProcessBackendClient
