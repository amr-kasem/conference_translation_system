from dataclasses import dataclass
from typing import  Optional

from domain.value_objects.language import LanguageData

@dataclass(frozen=True)
class UserData:
    id: Optional[str]
    name: Optional[str]
    home_language: LanguageData  # Language is now an enum
