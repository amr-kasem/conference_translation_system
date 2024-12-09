from datetime import datetime
from dataclasses import replace
from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.join_request import JoinRequest
from domain.usecases.usecase import Usecase
class JoinConference(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,request:JoinRequest)->None:
        attendance = request.attendence
        mod = replace(attendance, start=datetime.now())
        self.repo.add_user_to_conference(attendance=mod, conference_id=request.conference_id)