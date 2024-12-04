from injector import inject
from domain.usecases.migrate import Migrate


class MigrationServices:
    @inject
    def __init__(self,migrate: Migrate):
        self.migrate = migrate
        
    def migrate(self):
        self.migrate()
        