from injector import inject

from domain.usecases.conference.get_conference import GetConference
from domain.usecases.conference.initialize_conference import InitializeConference
from domain.value_objects.intialize_conference_request import InitializeConferenceRequest
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.usecases.usecase import Usecase
class StartConference(Usecase):
    @inject
    def __init__(self, get_conference:GetConference,init:InitializeConference, repository:ConferenceManagementRepository):
        self.get_conference = get_conference
        self.init = init
        self.repo = repository
    def __call__(self, req: InitializeConferenceRequest) -> None:
        conf = self.get_conference(req.conference_id)
        if conf:
            if not conf.isInitialized():
                self.init(req=req)
                conf = self.get_conference(req.conference_id)
            conf.start()
            self.repo.cache_conference(conf)
            self.repo.update_conference(conf)                           
        else:
            raise Exception('Error: Conference not found')