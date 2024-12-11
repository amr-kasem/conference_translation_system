from dataclasses import dataclass
from typing import Optional
@dataclass(frozen=True)  # Makes the class immutable
class TranslationResult:
    conference_id: Optional[str]  # User's name (string)
    language_id: str
    text: str
    voice: Optional[str]
