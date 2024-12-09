from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.entities.conference import Conference
from domain.usecases.usecase import Usecase
class GetConference(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self, id) -> Conference:
        conf = self.repo.get_cached_conference(id)
        if conf is None:
            conf = self.repo.get_conference(id)    
        return conf    