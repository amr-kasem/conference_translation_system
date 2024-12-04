from injector import inject

from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.usecases.usecase import Usecase
class Migrate(Usecase):
    @inject
    def __init__(self, repository:ConferenceManagementRepository):
        self.repo = repository

    def __call__(self,_:None=None):
        self.repo.migrate_db()