from typing import Iterator
from abc import ABC, abstractmethod

class StreamingInferenceDatasource(ABC):
    """
    Abstract base class for streaming inference data sources.
    This class handles text transcriptions, translations, voice links,
    and methods to publish source/translated text and audio streams.
    """

    @abstractmethod
    def transcriptions(self) -> Iterator[str]:
        """
        Iterator to retrieve transcriptions (converted speech to text) as a stream.
        Each element should be a string representing a transcribed sentence or word.
        """
        pass

    @abstractmethod
    def translations(self) -> Iterator[str]:
        """
        Iterator to retrieve translations for the transcribed text.
        Each element should be the translated string of the corresponding transcribed text.
        """
        pass

    @abstractmethod
    def voices(self) -> Iterator[str]:
        """
        Iterator to retrieve the URLs or HTTP links for the generated voice (audio).
        Each element should be a URL pointing to the audio file for the translation text.
        """
        pass

    @abstractmethod
    def publish_voice(self, voice_url: str) -> None:
        """
        Publish a stream of generated voice. This method sends the generated audio URL
        to an output destination (e.g., for playback, storage, or further processing).
        """
        pass

    @abstractmethod
    def publish_source_text(self, source_text: str) -> None:
        """
        Publish the source text that needs to be translated. This could be a transcription
        received from the ASR system that will be passed into the translation pipeline.
        """
        pass

    @abstractmethod
    def publish_translated_text(self, translated_text: str) -> None:
        """
        Publish the translated text that needs to be narrated or processed further.
        This is the output from the translation system before passing to TTS for voice synthesis.
        """
        pass
