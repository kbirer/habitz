
class Constants():
    """Class to contain compile time constants. 
        
    Attributes:

    ConfigFilePath -- Path to configuration file
    DatePickerFormat -- format of application wide dates"""
    config_file_path: str = 'config.ini'
    date_picker_format: str = '%d/%m/%Y'

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
        storage_section: str = 'DATA_STORAGE'
        backend_client_section: str = 'BACKEND_CLIENT'
        storage_type: str = 'StorageType'
        csv_habit_storage_file_path: str = 'CsvHabitStorageFilePath'
        csv_checked_out_habit_storage_file_path: str = 'CsvCheckedOutHabitStorageFilePath'
        clear_and_seed_data: str = 'ClearAndSeedData'
        sqlite_db_path: str = 'SqliteDbPath'
        client_type: str = 'ClientType'
        
    class HabitCsvFileColumnIndexes():
        """Inner class to contain compile time constants of habits csv file column indexes. 
            
        Attributes:

        Id -- Index for id field of habit data
        Name -- Index for name field of habit data
        Periodicity -- Index for periodicity field of habit data
        Times -- Index for times field of habit data"""
        id: int = 0
        name: int = 1
        periodicity: int = 2
        times: int = 3