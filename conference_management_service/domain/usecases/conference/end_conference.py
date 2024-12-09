from injector import inject

from dataclasses import replace
from datetime import datetime
from domain.usecases.conference.get_conference import GetConference
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.usecases.usecase import Usecase
class StopConference(Usecase):
    @inject
    def __init__(self, get_conference:GetConference, repository:ConferenceManagementRepository):
        self.get_conference = get_conference
        self.repo = repository
    def __call__(self, id: str) -> None:
        conf = self.get_conference(id)
        conf.stop()
        self.repo.cache_conference(conf)
        self.repo.update_conference(conf)
