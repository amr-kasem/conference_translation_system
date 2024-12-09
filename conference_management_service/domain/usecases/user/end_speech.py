from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.stop_speaking_request import StopSpeakingRequest
from domain.usecases.conference.get_conference import GetConference
from domain.usecases.usecase import Usecase
class FinishSpeech(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository, get_conf: GetConference):
        self.repo = repository
        self.get_conference = get_conf
    def __call__(self,req:StopSpeakingRequest) -> bool:
        conf = self.get_conference(req.conference_id)
        if conf:
            conf.finish_speach(attendance_id=req.attendence)
            return True
        else:
            return False