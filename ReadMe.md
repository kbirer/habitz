1. Install python 3.12 or greater or make sure you have it.<br>
2. Clone https://github.com/kbirer/habitz.git repo or extract the zip file to a directory.<br>
3. Assuming you have python installed, open a command prompt and navigate to project's directory. Create a virtual evnironment by running the following command **python3 -m venv .venv**<br>
4. Activate virtual environment by running **.venv\Scripts\Activate.bat**<br>
5. Run **pip install -r requirements.txt** command to install dependencies for the project<br>
6. Execute **python main.py** to start the application<br>
7. While in the root directory of the application and virtual environment activated type **pytest tests/ -n 16 -v** to run tests.<br>

This application is run through command line interface (cli). It presents series of options like<br>

1- Option 1<br>
2- Option 2<br>

and ask user to pick up an option. User must enter the option number printed on the start of each line to interact with application. Then based on the selected option the application is going to printout what user asked or it's going to present other options.<br>

Insted of entering the desired option number user can enter keyword **exit** to exit the application any time.<br>

This application uses a configuration file located in config.ini file to work accordingly. Description of each fields are described below:<br>

1. **DATA_STORAGE** Section:
   
    a. **StorageType**: Storage type value must be csv because other storage types not supported right now.<br>
    b. **CsvHabitStorageFilePath**: Csv storage file path to store habits. Default value is **Data/HabitDefinitions.csv** which is under Data folder of application's root folder.<br>
    c. **CsvCheckedOutHabitStorageFilePath**: Csv storage file path to store checkedout habits. Default value is **Data/CheckedoutHabits.csv** which is under Data folder of application's root folder.<br>
    d. **SqliteDbPath**: Not used since only csv storage type is supported for now.<br>
    e. **ClearAndSeedData**: A boolean value (True or False) which clears the storage (files in **CsvHabitStorageFilePath** and **CsvCheckedOutHabitStorageFilePath** configuration values) and creates new storage based on hardcoded test data. Warning if you enter, modify data, exit the application and leave this field to True then when you run application again, your data will be erased and default test data will be recreated again. Don't forget to set this field to False to avoid your data erased.<br>
   
3. **BACKEND_CLIENT** Section:<br>
    a. **ClientType**: Specifies the backend client used by ui layer. Only **InProcess** backend client is available for now.<br>

**Known Issues:**<br>
1. Sqlite or other rdms implementations should be implemented for faster performance.<br>
2. Pandas utilization should be improved for faster csv implementation.<br>
3. Unit tests should run flawlesly without having each of them run in a seperate process. Somehow mocking **configparser.open** keeping previous tests return value on the next test and causes it to fail. But there're 16 tests and creating 16 workers while running pytest or running.<br>
4. Layered architecture should be implemented for seperation of concerns and better maintenance.<br>
