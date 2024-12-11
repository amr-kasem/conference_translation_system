from dataclasses import replace
from injector import inject
from domain.repositories.translation_repository import TranslationRepository
from domain.usecases.translation.handle_translation import HandleTranslation
from domain.value_objects.init_vad_request import InitVadRequest
from domain.usecases.usecase import Usecase
class InitVad(Usecase):
    @inject
    def __init__(
        self,
        translation_repo:TranslationRepository,
        handle_translation: HandleTranslation,
        ):
        self.translation_repo = translation_repo 
        self.translate = handle_translation
    def __call__(self,req: InitVadRequest)->None:
        req = replace(req,on_voice_recieved=self.translate)
        self.translation_repo.init_vad(req=req)