from dataclasses import dataclass
@dataclass(frozen=True)  # Makes the class immutable
class TranslationDto:
    text: str
    voice: str