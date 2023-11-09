from Common.Config import Config
from Business.BackendClientFactory import BackendClientFactory
from Views.ViewManager import ViewManager

viewManager = ViewManager()

print('Welcome to Habitz, a habit tracking application')
print('Type exit to exit any time')
client = BackendClientFactory.CreateBackendClient()
if Config().ClearAndSeedData:
    print('Clearing and seeding data')
    client.ClearAndSeedData()

viewManager.Start()