import asyncio
import nats
from injector import inject

from typing import Callable
from domain.value_objects.vad_request import VadRequest
from infrastructure.data_sources.vad.vad_datasource import VadDataSource

class NatsVadDataSource(VadDataSource):
    @inject
    def __init__(self):
        self.nats_client = None
        self.connected = False
        self.voice_callback : Callable = None
        self.audio_subject = 'vad.audio'
        self.voice_subject = 'vad.voice'

    def init(self,voice_callback: Callable, host: str='localhost', port: int =4222):
        self.nats_url = f"nats://{host}:{port}"
        self.voice_callback = voice_callback
        asyncio.create_task(self.connect())

        
    async def connect(self):
        """Connect to the NATS server and subscribe to a subject."""
        self.nats_client = await nats.connect(self.nats_url)
        self.connected = True
        print(f"Connected to NATS at {self.nats_url}")
        self.voice_subscriber = await self.nats_client.subscribe(self.voice_subject, cb=self.digest_chunk)

    def close(self):
        """Gracefully close the NATS client connection."""
        if self.nats_client:
            self.voice_subscriber.unsubscribe()
            asyncio.create_task(self.nats_client.close())
            self.connected = False
            print("NATS connection closed.")

    def forward_chunk(self, req: VadRequest):
        asyncio.create_task(self.nats_client.publish(self.audio_subject, req))
            
    def digest_chunk(self,msg):
        print(f"Received message: {msg.data.decode()}")
        data = msg.data.decode()
        # must pass conference id and voice
        self.voice_callback(data)