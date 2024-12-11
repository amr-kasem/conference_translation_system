from fastapi import  HTTPException

from injector import inject

from domain.usecases.language.get_languages import GetLanguages
from domain.usecases.language.add_language import AddLanguage
from domain.usecases.language.delete_language import DeleteLanguage
from presentation.api.dtos.language.add_language import AddLanguageDto
from presentation.api.mappers.language_mapper import LanguageDtoMapper
from presentation.api.dtos.language.delete_language import DeleteLanguageDto

class LanguageController:
    @inject
    def __init__(
                    self,
                    add_language: AddLanguage,
                    get_languages: GetLanguages,
                    delete_language: DeleteLanguage,
                    language_mapper: LanguageDtoMapper,
                 ) -> None:
        self.add_language = add_language
        self.get_languages = get_languages
        self.delete_language = delete_language
        self.language_mapper = language_mapper


    async def add_language_handler(self, dto:AddLanguageDto):
        """Endpoint to add new language."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            language = self.language_mapper.to_language(dto=dto)
            self.add_language(language=language)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        
        
    async def get_languages_handler(self):
        """Endpoint to add new language."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            langs = self.get_languages()
            languages = [self.language_mapper.to_dto(language) for language in langs] 
            # Return success response
            return languages
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")
        
    async def delete_language_handler(self, language_id: str):
        """Endpoint to add new language."""
        try:
        # For simplicity, let's simulate a user registration
        # This can be replaced with actual logic such as saving to a database
            self.delete_language(language_id=language_id)
            # Return success response
            return {"message": 'success'}
        except Exception as e:
            # Handle any exceptions and raise HTTP 503 service unavailable error
            raise HTTPException(status_code=503, detail=f"Error registering user: {str(e)}")