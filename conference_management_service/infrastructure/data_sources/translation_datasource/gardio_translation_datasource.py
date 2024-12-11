from io import BytesIO
from typing import Tuple
from gradio_client import Client, handle_file

from conference_management_service.domain.value_objects.language import LanguageData
from conference_management_service.domain.value_objects.translation_result import TranslationResult

class GardioTranslationDatasouce:
    """
    Abstract base class for streaming inference data sources.
    This class handles text transcriptions, translations, voice links,
    and methods to publish source/translated text and audio streams.
    """

    def init(self,host:str,port:int):
        self.host = host
        self.port = port
        self.client = Client(f"http://{self.host}:{self.port}/")

    
    def translate(self, voice: BytesIO, src: LanguageData, dest: LanguageData) -> Tuple:
        task = '/s2' + task
        task = task + ('s' if dest.tts else 't')
        task = task + 't'
        
        result = self.client.predict(
            input_audio=voice,#handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),
            source_language=src.name,
            target_language=dest.name,
            api_name=task
        )
        
        return result
