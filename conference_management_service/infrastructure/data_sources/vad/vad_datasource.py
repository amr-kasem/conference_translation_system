from typing import Callable
from domain.value_objects.vad_request import VadRequest
from injector import inject

class VadDataSource:
    @inject
    def __init__(self):
        pass

    def init(self, voice_callback: Callable, host: str, port: int):
        """Initialize vad data souce connection parameters."""

    def close(self):
        """Gracefully close the client connection."""

    def forward_chunk(self, req: VadRequest):
        """Forward chunk to vad"""
        
    def digest_chunk(self,conference_id:str):
        """Callback on voice recieved"""