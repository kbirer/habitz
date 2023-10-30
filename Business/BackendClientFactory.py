from Business.IBackendClient import IBackendClient
from Business.InProcessBackendClient import InProcessBackendClient
from Common.Config import Config
from Storage.StorageFactory import StorageFactory

class BackendClientFactory():

    @staticmethod
    def CreateBackendClient() -> IBackendClient:
        match Config().ClientType:
            case 'InProcess':
                return InProcessBackendClient(StorageFactory.CreateStorage())
            case _:
                raise Exception('Not implemented backend client %s' % Config().ClientType)