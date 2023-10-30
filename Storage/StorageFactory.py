from Common.Config import Config
from Storage.CsvFileStorage import CsvFileStorage
from Storage.IStorage import IStorage
from Storage.SqliteStorage import SqliteStorage


class StorageFactory():

    @staticmethod
    def CreateStorage() -> IStorage:
        match Config().StorageType:
            case 'csv':
                return CsvFileStorage(Config().CsvHabitStorageFilePath, Config().CsvCheckedOutHabitStorageFilePath)
            case 'sqlite':
                return SqliteStorage()
            case _:
                raise Exception('Not implemented data storage %s' % Config().StorageType)
