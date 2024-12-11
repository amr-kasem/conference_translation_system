from dataclasses import dataclass
from io import BytesIO

@dataclass(frozen=True)  # Makes the class immutable
class TranslationRequest:
    conference_id: str
    voice: BytesIO
