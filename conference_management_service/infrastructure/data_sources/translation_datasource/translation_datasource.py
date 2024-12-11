from abc import ABC, abstractmethod
from io import BytesIO
from typing import Tuple

from domain.value_objects.language import LanguageData

class TranslationDataSource(ABC):
    """
    Abstract base class for streaming inference data sources.
    This class handles text transcriptions, translations, voice links,
    and methods to publish source/translated text and audio streams.
    """

    @abstractmethod
    def init(self,host:str,port:int):
        pass
    
    @abstractmethod
    def translate(self, voice: BytesIO, src: LanguageData, dest: LanguageData) -> Tuple:
        pass