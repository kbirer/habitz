from business.ibackend_client import IBackendClient
from business.in_process_backend_client import InProcessBackendClient
from common.config import Config
from storage.storage_factory import StorageFactory


class BackendClientFactory():
    """Backend client factory class is responsible for creating implementation of IBackendClient by ClientType attribute of Configuration"""
    @staticmethod
    def create_backend_client() -> IBackendClient:
        """A static factory method to create IBackendClient implementation. It's specified in BACKEND_CLIENT section and ClientType field of config.ini file.
        This field must be InProcess for the backend client running inside the same process

        Throws:
            Exception if ClientType attribute is not InProcess"""
        match Config().client_type:
            case 'InProcess':
                return InProcessBackendClient(StorageFactory.create_storage())
            case _:
                raise Exception(
                    'Not implemented backend client %s' %
                    Config().client_type)
