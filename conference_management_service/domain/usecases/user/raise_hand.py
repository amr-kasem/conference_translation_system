from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.raise_hand_request import RaiseHandRequest
from domain.usecases.conference.get_conference import GetConference
from domain.usecases.usecase import Usecase
class RaiseHand(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository, get_conf: GetConference):
        self.repo = repository
        self.get_conference = get_conf
    def __call__(self,req:RaiseHandRequest) -> bool:
        att = self.repo.get_attendance(attendance_id=req.attendence)
        conf = self.get_conference(req.conference_id)
        if conf:
            conf.raise_hand(att)
            return True
        else:
            return False