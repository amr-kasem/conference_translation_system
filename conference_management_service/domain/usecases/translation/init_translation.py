from injector import inject
from domain.repositories.translation_repository import TranslationRepository
from domain.value_objects.init_translation_request import InitTranslationRequest
from domain.usecases.usecase import Usecase
class InitTranslation(Usecase):
    @inject
    def __init__(
        self,
        translation_repo:TranslationRepository,
        ):
        self.translation_repo = translation_repo 
    def __call__(self,req: InitTranslationRequest)->None:
        self.translation_repo.init_translate(req=req)