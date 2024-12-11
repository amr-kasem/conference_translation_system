from injector import inject
from domain.usecases.usecase import Usecase
from domain.value_objects.vad_request import VadRequest
from domain.repositories.translation_repository import TranslationRepository
class ForwardChunk(Usecase):
    @inject
    def __init__(
        self,
        translation_repo:TranslationRepository,
    ):
        self.translation_repo = translation_repo 
    def __call__(self, req: VadRequest)->None:
        self.translation_repo.forward_chunk(req)