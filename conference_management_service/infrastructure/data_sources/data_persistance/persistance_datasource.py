from abc import ABC, abstractmethod
from typing import List, Optional
from infrastructure.dtos.sql_alchemy_models.attendance import AttendanceModel
from infrastructure.dtos.sql_alchemy_models.conference import ConferenceModel
from infrastructure.dtos.sql_alchemy_models.user import UserModel
from domain.value_objects.user import UserData
from domain.value_objects.language import LanguageData
from domain.entities.conference import Conference
# Abstract Base DataSource class for Conferences and Users
class PersistanceDataSource(ABC):
    @abstractmethod
    def get_conferences(self) -> List[ConferenceModel]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    
    @abstractmethod
    def get_conference(self, conference_id: str) -> ConferenceModel:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    
    @abstractmethod
    def add_new_conference(self, conference: ConferenceModel) -> None:
        """
        Add a new conference.
        Takes a Conference object and adds it to the data source.
        """
        pass

    @abstractmethod
    def update_conference(self, conference:ConferenceModel) -> bool:
        """
        Update a conference's name based on the conference ID.
        Returns True if the conference was updated, False if not found.
        """
        pass

    @abstractmethod
    def delete_conference(self, conference_id: str) -> bool:
        """
        Delete a conference based on the conference ID.
        Returns True if the conference was deleted, False if not found.
        """
        pass


    @abstractmethod
    def add_user(self, user: UserModel) -> None:
        """
        Add a user to a specific conference.
        """
        pass

    @abstractmethod
    def get_users(self, conference_id: int) -> List[UserData]:
        """
        Retrieve the list of users in a specific conference.
        """
        pass

    @abstractmethod
    def update_user(self, user_id: int, new_name: str) -> bool:
        """
        Update a user's name based on the user ID.
        Returns True if the user was updated, False if not found.
        """
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """
        Remove a user from a specific conference.
        Returns True if the user was deleted, False if not found.
        """
        pass

   
        pass

    @abstractmethod
    def add_user_to_conference(self, attendance: AttendanceModel) -> None:
        """
        Add a user to a conference, with the user's language and conference details.
        """
        pass

    @abstractmethod
    def get_attendees_for_conference(self, conference_id: str) -> List[Conference]:
        """
        Get all attendees for a specific conference.
        """
        pass

    @abstractmethod
    def exit_user_from_conference(self, user_id: str, conference_id: str) -> bool:
        """
        Remove a user from a specific conference.
        Returns True if the user was removed, False if not found.
        """
        pass

    @abstractmethod
    def update_user_in_conference(self, user_id: str, conference_id: str, new_language: LanguageData) -> bool:
        """
        Update a user's language in a conference.
        """
        pass
    @abstractmethod
    def get_attendance(self, attendance_id) -> Optional[AttendanceModel]:
        pass
    def add_language(self, language: LanguageData) -> None:
        """
        Add a user to a specific conference.
        """
        pass
    
    def delete_language(self, language_id: str) -> None:
        """
        Add a user to a specific conference.
        """
        pass
    
    def get_languages(self) -> list[LanguageData]:
        """
        Add a user to a specific conference.
        """
        pass
    

    @abstractmethod
    def migrate_db(self) -> bool:
        """
        delete and recreate translator_db.
        """
        