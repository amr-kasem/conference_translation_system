from abc import ABC, abstractmethod
from io import BytesIO

from domain.value_objects.language import LanguageData
from domain.value_objects.translation_result import TranslationResult
from domain.value_objects.init_translation_request import InitTranslationRequest
from domain.value_objects.vad_request import VadRequest
from domain.value_objects.init_vad_request import InitVadRequest
# from typing import List
# from infrastructure.dtos. import Conference
# Abstract Base DataSource class for Conferences and Users
class TranslationRepository(ABC):
    @abstractmethod
    def init_vad(self, req: InitVadRequest) -> None:
        """
        Initialize Voice Activity Detection (VAD).
        This method prepares the system to detect and process speech-to-text data. 
        It should be called before starting to transcribe or translate audio.
        """
        pass

    @abstractmethod
    def stop_vad(self) -> None:
        """
        Stop Voice Activity Detection (VAD).
        This method halts the speech-to-text conversion process and releases any resources used.
        """
        pass
    
    
    @abstractmethod
    def forward_chunk(self, req: VadRequest) -> None:
        """
        Forward a chunk of original voice.
        """
        pass


    @abstractmethod
    def init_translate(self, req: InitTranslationRequest) -> None:
        """
        Initialize translation for the provided source text.
        This method begins the process of translating a given text, which could be a transcription 
        from speech-to-text, into the desired language or format.
        """
        pass

    @abstractmethod
    def translate(self, voice: BytesIO, src: LanguageData, dest: LanguageData) -> TranslationResult:
        """
        Generate and publish translated audio from a given URL.
        This method triggers the conversion of a translated text into speech, which is made available via a URL.
        The generated audio can be used for playback, storage, or further processing.
        """
        pass
