from abc import ABC, abstractmethod
from typing import List
from domain.value_objects.language import LanguageData
from domain.value_objects.attendance_data import AttendanceData
from domain.value_objects.register_user import UserRegister
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
    def add_new_conference(self, conference: Conference) -> None:
        """
        Add a new conference.
        Takes a Conference object and adds it to the data source.
        """
        pass

    @abstractmethod
    def update_conference(self, conference_id: int, new_name: str) -> bool:
        """
        Update a conference's name based on the conference ID.
        Returns True if the conference was updated, False if not found.
        """
        pass

    @abstractmethod
    def delete_conference(self, conference_id: int) -> bool:
        """
        Delete a conference based on the conference ID.
        Returns True if the conference was deleted, False if not found.
        """
        pass


    @abstractmethod
    def add_user(self, user: UserRegister) -> None:
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
    def add_user_to_conference(self, attendance: AttendanceData) -> None:
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
        
    def add_language(self, language: LanguageData) -> None:
        """
        Add a user to a specific conference.
        """
        pass
    
    def delete_language(self, language: LanguageData) -> None:
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
        
        
