
class Constants():
    ConfigFilePath: str = 'config.ini'
    DatePickerFormat: str = '%d/%m/%Y'

    class ConfigurationKeys():
        StorageSection: str = 'DATA_STORAGE'
        BackendClientSection: str = 'BACKEND_CLIENT'
        StorageType: str = 'StorageType'
        CsvHabitStorageFilePath: str = 'CsvHabitStorageFilePath'
        CsvCheckedOutHabitStorageFilePath: str = 'CsvCheckedOutHabitStorageFilePath'
        ClearAndSeedData: str = 'ClearAndSeedData'
        SqliteDbPath: str = 'SqliteDbPath'
        ClientType: str = 'ClientType'
        
    class HabitCsvFileColumnIndexes():
        Id: int = 0
        Name: int = 1
        Periodicity: int = 2
        Times: int = 3