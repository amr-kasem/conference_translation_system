from typing import Iterator
from abc import ABC, abstractmethod

class GardioTranslationDatasouce(ABC):
    """
    Abstract base class for streaming inference data sources.
    This class handles text transcriptions, translations, voice links,
    and methods to publish source/translated text and audio streams.
    """

    