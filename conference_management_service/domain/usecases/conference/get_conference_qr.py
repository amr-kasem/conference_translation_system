from io import BytesIO
from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.usecases.usecase import Usecase
class GetConferenceQr(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,id:str)->BytesIO:
        return self.repo.get_qr_for_conference(conference_id=id)