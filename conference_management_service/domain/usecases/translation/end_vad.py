from injector import inject
from domain.usecases.usecase import Usecase
from domain.repositories.translation_repository import TranslationRepository
from domain.usecases.translation.handle_translation import HandleTranslation
class EndVad(Usecase):
    @inject
    def __init__(
        self,
        translation_repo:TranslationRepository,
    ):
        self.translation_repo = translation_repo 
    def __call__(self)->None:
        self.translation_repo.stop_vad()