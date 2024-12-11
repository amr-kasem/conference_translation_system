from presentation.api.dtos.language.language import LanguageDto
from presentation.api.dtos.language.add_language import AddLanguageDto
from domain.value_objects.language import LanguageData


class LanguageDtoMapper:
    def to_language(self,dto: AddLanguageDto) -> LanguageData:
        data = LanguageData(
            id=None,
            name=dto.name,
            translation_id=dto.translation_id,
            t2t=dto.t2t,
            asr=dto.asr,
            tts=dto.tts,
        )
        return data
    
    def to_dto(self,language: LanguageData) -> LanguageDto :
        dto = LanguageDto(
            id=language.id,
            name=language.name,
            translation_id=language.translation_id,
            t2t=language.t2t,
            asr=language.asr,
            tts=language.tts,
        )
        return dto
    