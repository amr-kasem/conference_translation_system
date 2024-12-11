from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.entities.conference import Conference
from domain.usecases.usecase import Usecase
class AddConference(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,conference:Conference)->None:
        self.repo.add_conference(conference=conference)