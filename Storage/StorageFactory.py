from Common.Config import Config
from Storage.CsvFileStorage import CsvFileStorage
from Storage.IStorage import IStorage
from Storage.SqliteStorage import SqliteStorage


class StorageFactory():
    """Factory method class for storage implementation"""

    @staticmethod
    def CreateStorage() -> IStorage:
        """Function to create storage implementation based on configuration
        
        Returns:
        
        Storage implementation which implements IStorage protocol class
        """
        match Config().StorageType:
            case 'csv':
                return CsvFileStorage(Config().CsvHabitStorageFilePath, Config().CsvCheckedOutHabitStorageFilePath)
            case 'sqlite':
                return SqliteStorage()
            case _:
                raise Exception('Not implemented data storage %s' % Config().StorageType)
