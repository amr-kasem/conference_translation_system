from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.language import LanguageData
from domain.usecases.usecase import Usecase
class DeleteLanguage(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,language_id:str)->None:
        self.repo.delete_language(language_id=language_id)