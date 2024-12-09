from dataclasses import dataclass
from typing import Optional
@dataclass(frozen=True)  # Makes the class immutable
class TranslationResult:
    id: Optional[str]  # User's name (string)
