from dataclasses import dataclass
from typing import Optional
@dataclass(frozen=True)  # Makes the class immutable
class LanguageData:
    id: Optional[str]  # User's name (string)
    name: Optional[str]  # User's language (Type of the Language class)
    translation_id: Optional[str]
    t2t: Optional[bool]
    asr: Optional[bool]
    tts: Optional[bool]