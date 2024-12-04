from injector import inject

from typing import List
from infrastructure.data_sources.data_persistance.persistance_datasource import PersistanceDataSource
from infrastructure.mappers.user_register_mapper import UserRegisterModelMapper
from infrastructure.mappers.language_model_mapper import LanguageModelMapper
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.language import LanguageData
from domain.value_objects.attendance_data import AttendanceData
from domain.value_objects.register_user import UserRegister
from domain.value_objects.user import UserData
from domain.entities.conference import Conference

# Abstract Base DataSource class for Conferences and Users
class ConferenceManagementRepositoryImpl(ConferenceManagementRepository):
    @inject
    def __init__(self,
                 data_source:PersistanceDataSource,
                 user_register_mapper:UserRegisterModelMapper,
                 language_mapper: LanguageModelMapper,
                ):
        self.data_source = data_source
        self.register_mapper = user_register_mapper
        self.language_mapper = language_mapper
    def get_conferences(self) -> List[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        pass
    

    def add_new_conference(self, conference: Conference) -> None:
        """
        Add a new conference.
        Takes a Conference object and adds it to the data source.
        """
        
        self.data_source.add_new_conference(conference=conference)
        pass


    def update_conference(self, conference_id: int, new_name: str) -> bool:
        """
        Update a conference's name based on the conference ID.
        Returns True if the conference was updated, False if not found.
        """
        pass


    def delete_conference(self, conference_id: int) -> bool:
        """
        Delete a conference based on the conference ID.
        Returns True if the conference was deleted, False if not found.
        """
        pass



    def add_user(self, user: UserRegister) -> None:
        """
        Register new user
        """
        print(user)
        model = self.register_mapper.to_model(user)
        
        self.data_source.add_user(user=model)


    def get_users(self, conference_id: int) -> List[UserData]:
        """
        Get all users
        """
        pass


    def update_user(self, user_data: UserData) -> bool:
        """
        Update a user
        """
        pass


    def delete_user(self, user_data: UserData) -> bool:
        """
        Remove a user by id
        Returns True if the user was deleted, False if not found.
        """
        pass

   
        pass


    def add_user_to_conference(self, attendance: AttendanceData) -> None:
        """
        Add a user to a conference, with the user's language and conference details.
        """
        pass


    def get_attendees_for_conference(self, conference_id: str) -> List[AttendanceData]:
        """
        Get all attendees for a specific conference.
        """
        pass


    def exit_user_from_conference(self, user_id: str, conference_id: str) -> bool:
        """
        Remove a user from a specific conference.
        Returns True if the user was removed, False if not found.
        """
        pass


    def update_user_in_conference(self, user_id: str, conference_id: str, new_language: LanguageData) -> bool:
        """
        Update a user's language in a conference.
        """

    def add_language(self, language: LanguageData) -> None:
        """
        Add a user to a specific conference.
        """
        language_model = self.language_mapper.to_model(language)
        self.data_source.add_language(language=language_model)
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
    
        
    def migrate_db(self) -> bool:
        """
        delete and recreate translator_db.
        """
        self.data_source.migrate_db()
        