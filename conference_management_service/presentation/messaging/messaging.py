import nats
from injector import inject

from uuid import UUID
from domain.usecases.conference.initialize_conference import InitializeConference
from domain.usecases.translation.handle_translation import HandleTranslation
from presentation.messaging.conference_controller import ConferenceMessagingController

class MessagingServices:
    @inject
    def __init__(self,translate:HandleTranslation,init_conference: InitializeConference):
        self.nats_client = None
        self.connected = False
        self.conferences : dict[UUID,ConferenceMessagingController] = {}
        self.translate = translate
        self.init_conference = init_conference

    def init(self, host: str='localhost', port: int =4222):
        self.nats_url = f"nats://{host}:{port}"
        
    async def connect(self):
        """Connect to the NATS server and subscribe to a subject."""
        self.nats_client = await nats.connect(self.nats_url)
        self.connected = True
        print(f"Connected to NATS at {self.nats_url}")

    async def close(self):
        """Gracefully close the NATS client connection."""
        if self.nats_client:
            await self.nats_client.close()
            self.connected = False
            print("NATS connection closed.")

    def new_conference_controller(self, conference_id: str):
        if self.connected:
            controller = ConferenceMessagingController(
                nats_client = self.nats_client,
                conference_id = conference_id,
                handle_translation=self.translate,
                init_conference=self.init_conference,
            )
            self.conferences[UUID('{' + conference_id + '}')] = controller
            return True
        else:
            return False
            
    def remove_conference(self,conference_id:str):
        self.conferences.pop(UUID('{' + conference_id + '}'))