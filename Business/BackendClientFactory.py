from Business.IBackendClient import IBackendClient
from Business.InProcessBackendClient import InProcessBackendClient
from Common.Config import Config
from Storage.StorageFactory import StorageFactory

class BackendClientFactory():
    """Backend client factory class is responsible for creating implementation of IBackendClient by ClientType attribute of Configuration"""
    @staticmethod
    def CreateBackendClient() -> IBackendClient:
        """A static factory method to create IBackendClient implementation. It's specified in BACKEND_CLIENT section and ClientType field of config.ini file.
        This field must be InProcess for the backend client running inside the same process
        
        Throws:
            Exception if ClientType attribute is not InProcess"""
        match Config().ClientType:
            case 'InProcess':
                return InProcessBackendClient(StorageFactory.CreateStorage())
            case _:
                raise Exception('Not implemented backend client %s' % Config().ClientType)