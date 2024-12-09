import asyncio
from domain.usecases.conference.initialize_conference import InitializeConference
from domain.usecases.translation.handle_translation import HandleTranslation
from domain.value_objects.translation_result import TranslationResult

class ConferenceMessagingController:
    def __init__(
        self,
        nats_client,
        conference_id:str,
        handle_translation: HandleTranslation,
        init_conference: InitializeConference,
    ):
        self.translate = handle_translation
        self.initialize_conference = init_conference
        self.nats_client = nats_client
        self.conference_id = conference_id
        self.voice_topic = f"{self.conference_id}/voice"
        self.speaker_topic = f"{self.conference_id}/speaker"
        self.voice_subscriber = None
        
    async def start(self):
        self.voice_subscriber = await self.nats_client.subscribe(self.voice_topic, cb=self.voice_handler)

    async def voice_handler(self,msg):
        print(f"Received message: {msg.data.decode()}")
        res = []
        try:
            res = self.translate(TranslationResult(None))
        except:
            # self.initialize_conference()
            # res = self.translate(TranslationResult(None))
            print('ignored because conference is not started yet')
        await self.publish_translation(res)

    def speaker_callback(self, speaker_id: str):
        print(f'speaker_id will be published: {speaker_id}')
        asyncio.create_task(self.nats_client.publish(self.speaker_topic, speaker_id.encode()))

    async def publish_translation(self, translations: list[TranslationResult]):
        for t in translations:
            self.nats_client.publish(f'{self.conference_id}/translation/{t.id}', 'translated text'.encode())

    async def stop(self):
        if self.voice_subscriber is not None:
            await self.voice_subscriber.unsubscribe()
