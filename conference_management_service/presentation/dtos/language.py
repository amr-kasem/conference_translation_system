from pydantic import BaseModel

class LanguageDto(BaseModel):
    id: str  # User's name (string)
    name: str  # User's language (Type of the Language class)
    translation_id: str
    asr_id: str
    tts_id: str