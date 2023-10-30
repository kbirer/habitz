import configparser
from curses.ascii import isspace

from Common.Constants import Constants


class Config():
    StorageType: str = ''
    CsvHabitStorageFilePath: str = ''
    CsvCheckedOutHabitStorageFilePath: str = ''
    SqliteDbPath: str = ''
    ClearAndSeedData: bool = False
    ClientType: str = ''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
            config = configparser.ConfigParser()
            config.read(Constants.ConfigFilePath)

            storageSection = config[Constants.ConfigurationKeys.StorageSection]
            if config.has_option(Constants.ConfigurationKeys.StorageSection, Constants.ConfigurationKeys.CsvCheckedOutHabitStorageFilePath):
                cls.instance.CsvCheckedOutHabitStorageFilePath = storageSection[
                    Constants.ConfigurationKeys.CsvCheckedOutHabitStorageFilePath]
            if config.has_option(Constants.ConfigurationKeys.StorageSection, Constants.ConfigurationKeys.CsvHabitStorageFilePath):
                cls.instance.CsvHabitStorageFilePath = storageSection[
                    Constants.ConfigurationKeys.CsvHabitStorageFilePath]
            if config.has_option(Constants.ConfigurationKeys.StorageSection, Constants.ConfigurationKeys.SqliteDbPath):
                cls.instance.SqliteDbPath = storageSection[Constants.ConfigurationKeys.SqliteDbPath]
            if config.has_option(Constants.ConfigurationKeys.StorageSection, Constants.ConfigurationKeys.StorageType):
                cls.instance.StorageType = storageSection[Constants.ConfigurationKeys.StorageType]
            if config.has_option(Constants.ConfigurationKeys.StorageSection, Constants.ConfigurationKeys.ClearAndSeedData):
                cls.instance.ClearAndSeedData = bool(
                    storageSection[Constants.ConfigurationKeys.ClearAndSeedData])

            backendClientSection = config[Constants.ConfigurationKeys.BackendClientSection]
            if config.has_option(Constants.ConfigurationKeys.BackendClientSection, Constants.ConfigurationKeys.ClientType):
                    cls.instance.ClientType = backendClientSection[Constants.ConfigurationKeys.ClientType]
                                
            cls.instance.Validate()
        return cls.instance

    @staticmethod
    def RaiseErrorIfRequired(configKey: str, value: str) -> None:
        if not value:
            raise ValueError('%s parameter is required' % configKey)

    def Validate(self) -> None:
        Config.RaiseErrorIfRequired(
            Constants.ConfigurationKeys.StorageType, self.StorageType)
        if self.StorageType != 'csv' and self.StorageType != 'sqlite':
            raise ValueError('Storage type must be csv or sqlite')
        if self.StorageType == 'csv':
            Config.RaiseErrorIfRequired(
                Constants.ConfigurationKeys.CsvCheckedOutHabitStorageFilePath, self.CsvCheckedOutHabitStorageFilePath)
            Config.RaiseErrorIfRequired(
                Constants.ConfigurationKeys.CsvHabitStorageFilePath, self.CsvHabitStorageFilePath)
        if self.StorageType == 'sqlite':
            Config.RaiseErrorIfRequired(
                Constants.ConfigurationKeys.SqliteDbPath, self.SqliteDbPath)
        if self.ClientType != 'InProcess':
            raise ValueError(f'{Constants.ConfigurationKeys.ClientType} must be InProcess')
