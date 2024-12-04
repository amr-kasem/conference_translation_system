from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.language import LanguageData
from domain.usecases.usecase import Usecase
class RegisterUser(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,user_register:LanguageData):
        self.repo.add_language(user=user_register)