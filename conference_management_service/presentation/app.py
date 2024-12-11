from injector import inject
import uvicorn
from presentation.api.rest_api import  RestApi
from presentation.messaging.messaging import MessagingServices
from domain.value_objects.init_vad_request import InitVadRequest
from domain.value_objects.init_translation_request import InitTranslationRequest
from presentation.migrate import MigrationServices
from domain.usecases.translation.init_translation import InitTranslation
from domain.usecases.translation.init_vad import InitVad

class InstantTranslationApp:
    @inject
    def __init__(
        self,
        api:RestApi,
        messaging: MessagingServices,
        migration: MigrationServices,
        init_vad: InitVad,
        init_translation: InitTranslation
    ):
        self.api = api
        self.messaging = messaging
        self.migration = migration
        self.init_vad = init_vad
        self.init_translation = init_translation

    def start(
        self, 
        api_host:str="127.0.0.1",
        api_port:int=8000,
        messaging_host:str="localhost",
        messaging_port:int=4442,
        vad_host:str="localhost",
        vad_port:int=4442,
        translation_host:str="localhost",
        translation_port:int=7860,
    ):
        self.messaging.init(host=messaging_host,port=messaging_port)
        self.api.init(self.messaging)
        self.init_vad(
            req=InitVadRequest(
                vad_host=vad_host,
                vad_port=vad_port,
            )
        )
        self.init_translation(
            InitTranslationRequest(
                translation_host=translation_host,
                translation_port=translation_port,
            )
        )
        self.init_translation()
        uvicorn.run(self.api.get_app(), host=api_host, port=api_port)

    def migrate(self):
        self.migration.migrate()