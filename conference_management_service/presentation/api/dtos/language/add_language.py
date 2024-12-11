from pydantic import BaseModel

class AddLanguageDto(BaseModel):
    name: str  # User's language (Type of the Language class)
    translation_id: str
    t2t: bool
    asr: bool
    tts: bool