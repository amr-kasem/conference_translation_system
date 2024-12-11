from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.conference import Conference
# Abstract Base DataSource class for Conferences and Users
class InMemoryDataSource(ABC):
    @abstractmethod
    def get_conference(id:UUID) -> Conference:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass

    @abstractmethod
    def store_conference(conference: Conference) -> None:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    