import configparser
from common.constants import Constants


class Config():
    """Singleton class for loading configurations. 

    Attributes:

    StorageType -- Storage type of application.
    CsvHabitStorageFilePath -- Csv file path for habit definition storage.
    CsvCheckedOutHabitStorageFilePath -- Csv file path for checked out habit storage.
    SqliteDbPath -- Sqlite database file path for sqlite storage.
    ClearAndSeedData -- Clear and create new habit and checkout data
    ClientType -- Backend client type"""
    storage_type: str = ''
    csv_habit_storage_file_path: str = ''
    csv_checked_out_habit_storage_file_path: str = ''
    sqlite_db_path: str = ''
    clear_and_seed_data: bool = False
    client_type: str = ''

    def __new__(cls):
        """Singleton ctor."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
            config = configparser.ConfigParser()
            config.read(Constants.config_file_path)

            storage_section = config[Constants.ConfigurationKeys.storage_section]
            if config.has_option(
                    Constants.ConfigurationKeys.storage_section, Constants.
                    ConfigurationKeys.csv_checked_out_habit_storage_file_path):
                cls.instance.csv_checked_out_habit_storage_file_path = storage_section[
                    Constants.ConfigurationKeys.csv_checked_out_habit_storage_file_path]
            if config.has_option(
                    Constants.ConfigurationKeys.storage_section, Constants.
                    ConfigurationKeys.csv_habit_storage_file_path):
                cls.instance.csv_habit_storage_file_path = storage_section[
                    Constants.ConfigurationKeys.csv_habit_storage_file_path]
            if config.has_option(Constants.ConfigurationKeys.storage_section,
                                 Constants.ConfigurationKeys.sqlite_db_path):
                cls.instance.sqlite_db_path = storage_section[Constants.ConfigurationKeys.sqlite_db_path]
            if config.has_option(Constants.ConfigurationKeys.storage_section,
                                 Constants.ConfigurationKeys.storage_type):
                cls.instance.storage_type = storage_section[Constants.ConfigurationKeys.storage_type]
            if config.has_option(Constants.ConfigurationKeys.storage_section,
                                 Constants.ConfigurationKeys.clear_and_seed_data):
                cls.instance.clear_and_seed_data = storage_section[
                    Constants.ConfigurationKeys.clear_and_seed_data] == 'True'

            backend_client_section = config[Constants.ConfigurationKeys.backend_client_section]
            if config.has_option(
                    Constants.ConfigurationKeys.backend_client_section, Constants.
                    ConfigurationKeys.client_type):
                cls.instance.client_type = backend_client_section[Constants.ConfigurationKeys.client_type]

            cls.instance.validate()
        return cls.instance

    @staticmethod
    def raise_error_if_required(config_key: str, value: str) -> None:
        """Checkes and raises ValueError for required configurations."""
        if not value:
            raise ValueError('%s parameter is required' % config_key)

    def validate(self) -> None:
        """Validates if configuration data is valid."""
        Config.raise_error_if_required(
            Constants.ConfigurationKeys.storage_type, self.storage_type)
        if self.storage_type != 'csv' and self.storage_type != 'sqlite':
            raise ValueError('Storage type must be csv or sqlite')
        if self.storage_type == 'csv':
            Config.raise_error_if_required(
                Constants.ConfigurationKeys.csv_checked_out_habit_storage_file_path,
                self.csv_checked_out_habit_storage_file_path)
            Config.raise_error_if_required(
                Constants.ConfigurationKeys.csv_habit_storage_file_path, self.csv_habit_storage_file_path)
        if self.storage_type == 'sqlite':
            Config.raise_error_if_required(
                Constants.ConfigurationKeys.sqlite_db_path, self.sqlite_db_path)
        if self.client_type != 'InProcess':
            raise ValueError(
                f'{Constants.ConfigurationKeys.client_type} must be InProcess')
