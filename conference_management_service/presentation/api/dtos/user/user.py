from presentation.api.dtos.language.language import LanguageDto
from pydantic import BaseModel

class UserDto(BaseModel):
    id: str
    name: str
    home_language: LanguageDto 