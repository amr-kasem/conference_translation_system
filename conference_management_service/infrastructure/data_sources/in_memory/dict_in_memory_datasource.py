from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.conference import Conference
# Abstract Base DataSource class for Conferences and Users
class DictInMemoryDataSource(ABC):
    def __init__(self):
        self._cache = {}
    
    def get_conference(self,id:str) -> Conference | None:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        return self._cache.get(id)
        


    def store_conference(self,conference: Conference) -> None:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        self._cache[conference.data.id] = conference