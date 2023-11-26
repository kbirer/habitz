
class Constants():
    """Class to contain compile time constants. 
        
    Attributes:

    ConfigFilePath -- Path to configuration file
    DatePickerFormat -- format of application wide dates"""
    ConfigFilePath: str = 'config.ini'
    DatePickerFormat: str = '%d/%m/%Y'

    class ConfigurationKeys():
        """Inner class to contain compile time constants of configuration keys. 
            
        Attributes:

        StorageSection -- Configuration key for storage section of config.ini file
        BackendClientSection -- Configuration key for backend client section of config.ini file
        StorageType -- Configuration key for storage type
        CsvHabitStorageFilePath -- Configuration key for csv habit definitions file path
        CsvCheckedOutHabitStorageFilePath -- Configuration key for csv checkedout habits file path
        ClearAndSeedData -- Configuration key for enabling clearing and seeding data
        SqliteDbPath -- Configuration key for sqlite db path
        ClientType -- Configuration key for backend client type"""
        StorageSection: str = 'DATA_STORAGE'
        BackendClientSection: str = 'BACKEND_CLIENT'
        StorageType: str = 'StorageType'
        CsvHabitStorageFilePath: str = 'CsvHabitStorageFilePath'
        CsvCheckedOutHabitStorageFilePath: str = 'CsvCheckedOutHabitStorageFilePath'
        ClearAndSeedData: str = 'ClearAndSeedData'
        SqliteDbPath: str = 'SqliteDbPath'
        ClientType: str = 'ClientType'
        
    class HabitCsvFileColumnIndexes():
        """Inner class to contain compile time constants of habits csv file column indexes. 
            
        Attributes:

        Id -- Index for id field of habit data
        Name -- Index for name field of habit data
        Periodicity -- Index for periodicity field of habit data
        Times -- Index for times field of habit data"""
        Id: int = 0
        Name: int = 1
        Periodicity: int = 2
        Times: int = 3