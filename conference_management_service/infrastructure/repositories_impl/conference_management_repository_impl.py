from uuid import UUID, uuid4
from injector import inject

from typing import List, Optional
from io import BytesIO
from infrastructure.data_sources.qr_generator.qr_generator import QRcodeGenerator
from infrastructure.data_sources.data_persistance.persistance_datasource import PersistanceDataSource
from infrastructure.data_sources.in_memory.in_memory_datasource import InMemoryDataSource
from infrastructure.mappers.user_model_mapper import UserModelMapper
from infrastructure.mappers.attendance_model_mapper import AttendanceModelMapper
from infrastructure.mappers.conference_model_mapper import ConferenceModelMapper
from infrastructure.mappers.language_model_mapper import LanguageModelMapper
from domain.repositories.conference_management_repository import ConferenceManagementRepository
from domain.value_objects.language import LanguageData
from domain.value_objects.attendance_data import AttendanceData
from domain.value_objects.user import UserData
from domain.value_objects.user import UserData
from domain.entities.conference import Conference

# Abstract Base DataSource class for Conferences and Users
class ConferenceManagementRepositoryImpl(ConferenceManagementRepository):
    @inject
    def __init__(self,
                 data_source:PersistanceDataSource,
                 caching_source:InMemoryDataSource,
                 qr_generator: QRcodeGenerator,
                 user_register_mapper:UserModelMapper,
                 language_mapper: LanguageModelMapper,
                 attendance_mapper: AttendanceModelMapper,
                 conference_mapper: ConferenceModelMapper,
                ):
        self.data_source = data_source
        self.caching_source = caching_source
        self.qr_generator = qr_generator
        self.register_mapper = user_register_mapper
        self.language_mapper = language_mapper
        self.attendance_mapper = attendance_mapper
        self.conference_mapper = conference_mapper
        
    def get_conferences(self) -> List[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        confs = self.data_source.get_conferences()
        
        data = [
                Conference(data=self.conference_mapper.to_data(conf))
                for conf in confs
            ]

        return data
    
    
    def cache_conference(self, conference: Conference) -> None:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        self.caching_source.store_conference(conference)
    
    
    def get_conference(self, conference_id: str) -> Optional[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        model = self.data_source.get_conference(conference_id)
        return Conference(
            data=self.conference_mapper.to_data(model=model)
        )

    def get_cached_conference(self, conference_id: str) -> Optional[Conference]:
        """
        Retrieve the list of all conferences.
        Must return a list of Conference objects.
        """
        x = self.caching_source.get_conference(conference_id)
        return x
        

    def add_conference(self, conference: Conference) -> None:
        """
        Add a new conference.
        Takes a Conference object and adds it to the data source.
        """
        model = self.conference_mapper.to_model(conference.data)
        self.data_source.add_new_conference(conference=model)
        pass


    def update_conference(self, conference: Conference) -> bool:
        """
        Update a conference's name based on the conference ID.
        Returns True if the conference was updated, False if not found.
        """
        model = self.conference_mapper.to_model(conference.data)
        self.data_source.update_conference(conference=model)
        pass


    def delete_conference(self, conference_id: str) -> bool:
        """
        Delete a conference based on the conference ID.
        Returns True if the conference was deleted, False if not found.
        """
        pass
        self.data_source.delete_conference(conference_id=conference_id)

    def get_qr_for_conference(self, conference_id: str)-> BytesIO:

        return self.qr_generator.get_qr_for_conference(conference_id=conference_id)
        

    def add_user(self, user: UserData) -> None:
        """
        Register new user
        """
        model = self.register_mapper.to_model(user)
        
        self.data_source.add_user(user=model)


    def get_users(self) -> List[UserData]:
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


    def add_user_to_conference(self, attendance: AttendanceData, conference_id: str) -> None:
        """
        Add a user to a conference, with the user's language and conference details.
        """
        model = self.attendance_mapper.to_model(attendance)
        model.conference_id = conference_id
        self.data_source.add_user_to_conference(attendance=model)
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
        pass
    
    def get_attendance(self, attendance_id:str) -> Optional[AttendanceData]:
        model = self.data_source.get_attendance(attendance_id=attendance_id)
        if model:
            att = self.attendance_mapper.to_data(model)
            return att
        else:
            return None
        
    def add_language(self, language: LanguageData) -> None:
        """
        Add a language to supported languages.
        """
        language_model = self.language_mapper.to_model(language)
        self.data_source.add_language(language=language_model)
        pass
    
    def delete_language(self, language_id: str) -> None:
        """
        Delete a language by id.
        """
        self.data_source.delete_language(language_id=language_id)
        pass
    
    def get_languages(self) -> list[LanguageData]:
        """
        get all languages.
        """
        langs = self.data_source.get_languages()
        data = [self.language_mapper.to_data(language) for language in langs]
        return data
        
    
        
    def migrate_db(self) -> bool:
        """
        delete and recreate translator_db.
        """
        self.data_source.migrate_db()
        