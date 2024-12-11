import asyncio
import nats
from injector import inject

from domain.value_objects.speaker_change_data import SpeakerChangeData
from domain.value_objects.translation_result import TranslationResult
from presentation.messaging.dto.translation import TranslationDto
from domain.usecases.conference.initialize_conference import InitializeConference
from domain.usecases.translation.handle_translation import HandleTranslation

class MessagingServices:
    @inject
    def __init__(self,translate:HandleTranslation,init_conference: InitializeConference):
        self.nats_client = None
        self.connected = False
        self.translate = translate
        self.init_conference = init_conference

    def init(self, host: str='localhost', port: int =4222):
        self.nats_url = f"nats://{host}:{port}"
        self.translate.init(translation_callback=self.publish_translation)
        
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

    def speaker_callback(self, speaker_change_data: SpeakerChangeData):
        print(f'speaker_id will be published: {speaker_change_data.speaker_id}')
        asyncio.create_task(self.nats_client.publish(f'{speaker_change_data.conference_id}/speaker', speaker_change_data.speaker_id))
        
    def publish_translation(self, translations: list[TranslationResult]):
        for t in translations:
            asyncio.create_task(self.nats_client.publish(f'{t.conference_id}/translation/{t.language_id}', TranslationDto(text=t.text,voice=t.voice).encode()))
