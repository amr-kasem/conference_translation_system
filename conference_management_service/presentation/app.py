import uvicorn
from injector import inject
from presentation.api import ApiServices
from presentation.messaging import MessagingServices
from presentation.migrate import MigrationServices

class InstantTranslationApp:
    @inject
    def __init__(self,api:ApiServices,messaging: MessagingServices,migration: MigrationServices):
        self.api = api
        self.messaging = messaging
        self.migration = migration

    def start(
        self, 
        api_host:str="127.0.0.1",
        api_port:int=8000,
        messaging_host:str="localhost",
        messaging_port:int=4442
    ):
        self.messaging.init(host=messaging_host,port=messaging_port)
        self.api.init(self.messaging)
        uvicorn.run(self.api.get_app(), host=api_host, port=api_port)

    def migrate(self):
        self.migration.migrate()