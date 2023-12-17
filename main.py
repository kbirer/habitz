from common.config import Config
from business.backend_client_factory import BackendClientFactory
from views.view_manager import ViewManager

view_manager = ViewManager()

print('Welcome to Habitz, a habit tracking application')
print('Type exit to exit any time')
client = BackendClientFactory.create_backend_client()
if Config().clear_and_seed_data:
    print('Clearing and seeding data')
    client.clear_and_seed_data()

view_manager.start()
