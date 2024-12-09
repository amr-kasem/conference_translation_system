from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.conference import ConferenceData
from domain.usecases.usecase import Usecase
class GetConferences(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self) -> list[ConferenceData]:
        return self.repo.get_conferences()
        