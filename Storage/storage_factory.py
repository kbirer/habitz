from common.config import Config
from storage.csv_file_storage import CsvFileStorage
from storage.istorage import IStorage
from storage.sqlite_storage import SqliteStorage


class StorageFactory():
    """Factory method class for storage implementation"""

    @staticmethod
    def create_storage() -> IStorage:
        """Function to create storage implementation based on configuration
        
        Returns:
        
        Storage implementation which implements IStorage protocol class
        """
        match Config().storage_type:
            case 'csv':
                return CsvFileStorage(Config().csv_habit_storage_file_path, Config().csv_checked_out_habit_storage_file_path)
            case 'sqlite':
                return SqliteStorage()
            case _:
                raise Exception('Not implemented data storage %s' % Config().storage_type)
