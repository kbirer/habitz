from Common.Config import Config
from Storage.StorageFactory import StorageFactory
from UI.DateValuePicker import DateValuePicker
from UI.TextValuePicker import TextValuePicker
from Business.BackendClientFactory import BackendClientFactory

print('Welcome to Habitz, a habit tracking application')
client = BackendClientFactory.CreateBackendClient()
if Config().ClearAndSeedData:
    print('Clearing and seeding data')
    client.ClearAndSeedData()