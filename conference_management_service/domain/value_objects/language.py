from dataclasses import dataclass
@dataclass(frozen=True)  # Makes the class immutable
class LanguageData:
    id: str  # User's name (string)
    name: str  # User's language (Type of the Language class)
    translation_id: str
    t2t: bool
    asr: bool
    tts: bool
    # asr_id: str
    # tts_id: str