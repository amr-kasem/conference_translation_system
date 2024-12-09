from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.entities.conference import Conference
from domain.usecases.usecase import Usecase
class DeleteConference(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,conference_id:str)->None:
        self.repo.delete_conference(conference_id=conference_id)