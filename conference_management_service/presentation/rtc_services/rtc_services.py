from injector import inject
import asyncio
from typing import Callable
from domain.value_objects.speaker_change_data import SpeakerChangeData
from presentation.rtc_services.rtc_callee import WebRTCCallee
from domain.usecases.translation.forward_chunk import ForwardChunk

class RTCServices:
    @inject
    def __init__(self, forward_chunk:ForwardChunk) -> None:
        self.callees : dict[str,WebRTCCallee]= {}
        self.forward_chunk = forward_chunk
        self.on_speaker_change: Callable
        
    def init(self,on_speaker_change):
        self.on_speaker_change = on_speaker_change
    
    def add_callee(self, conference_id:str):
        callee = WebRTCCallee(conference_id=conference_id)
        asyncio.create_task(callee.initialize(on_chunk_callback=self.forward_chunk))
        callee.start()
        
        
    def remove_callee(self, conference_id):
        callee = self.callees[conference_id]
        asyncio.create_task(callee.close())
        self.callees.pop(conference_id)
        
        
    def change_speaker(self, speaker: SpeakerChangeData):
        callee = self.callees[speaker.conference_id]
        callee.change_speaker(speaker.speaker_id)