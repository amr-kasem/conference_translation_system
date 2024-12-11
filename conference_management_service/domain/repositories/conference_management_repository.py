from abc import ABC, abstractmethod
from io import BytesIO
from typing import List, Optional
from domain.value_objects.language import LanguageData
from domain.value_objects.attendance_data import AttendanceData
from domain.value_objects.user import UserData
from domain.value_objects.user import UserData
from domain.entities.conference import Conference
# Abstract Base DataSource class for Conferences and Users
class ConferenceManagementRepository(ABC):
    @abstractmethod
    def get_conferences(self) -> List[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    
    @abstractmethod
    def cache_conference(self, conference: Conference) -> None:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    
    @abstractmethod
    def get_conference(self, conference_id: str) -> Optional[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    
    @abstractmethod
    def get_cached_conference(self, conference_id: str) -> Optional[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    
    @abstractmethod
    def get_qr_for_conference(self, conference_id: str)-> BytesIO:
        pass
    
    @abstractmethod
    def add_conference(self, conference: Conference) -> None:
        """
        Add a new conference.
        Takes a Conference object and adds it to the data source.
        """
        pass

    @abstractmethod
    def update_conference(self, conference:Conference) -> bool:
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
    def add_user(self, user: UserData) -> None:
        """
        Register new user
        """
        pass

    @abstractmethod
    def get_users(self, conference_id: int) -> List[UserData]:
        """
        Get all users
        """
        pass

    @abstractmethod
    def update_user(self, user_data: UserData) -> bool:
        """
        Update a user
        """
        pass

    @abstractmethod
    def delete_user(self, user_data: UserData) -> bool:
        """
        Remove a user by id
        Returns True if the user was deleted, False if not found.
        """
        pass

   
        pass

    @abstractmethod
    def add_user_to_conference(self, attendance: AttendanceData, conference_id: str) -> None:
        """
        Add a user to a conference, with the user's language and conference details.
        """
        pass

    @abstractmethod
    def get_attendees_for_conference(self, conference_id: str) -> List[AttendanceData]:
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

    def get_attendance(self, attendance_id:str) -> Optional[AttendanceData]:
        pass
    def add_language(self, language: LanguageData) -> None:
        """
        Add a language to supported languages.
        """
        pass
    
    def delete_language(self, language_id: str) -> None:
        """
        Delete a language by id.
        """
        pass
    
    def get_languages(self) -> list[LanguageData]:
        """
        get all languages.
        """
        pass
    
    @abstractmethod
    def migrate_db(self) -> bool:
        """
        delete and recreate translator_db.
        """
        
        
