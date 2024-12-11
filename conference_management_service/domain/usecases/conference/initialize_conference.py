from injector import inject

from domain.value_objects.intialize_conference_request import InitializeConferenceRequest
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.entities.conference import Conference
from domain.usecases.usecase import Usecase
class InitializeConference(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,req: InitializeConferenceRequest) -> Conference:

        conf = self.repo.get_conference(req.conference_id)    
        if conf:
            conf.init(req.on_speaker_change)
            self.repo.cache_conference(conference=conf) 
        else: 
            raise Exception('Error: Conference not found') 
