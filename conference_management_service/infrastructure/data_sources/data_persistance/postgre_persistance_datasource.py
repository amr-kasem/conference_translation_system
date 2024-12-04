# Assuming the session and engine are already set up
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from infrastructure.dtos.sql_alchemy_models.attendance import AttendanceModel
from infrastructure.dtos.sql_alchemy_models.user import UserModel
from infrastructure.dtos.sql_alchemy_models.conference import ConferenceModel
from infrastructure.data_sources.data_persistance.persistance_datasource import PersistanceDataSource
from infrastructure.dtos.sql_alchemy_models.language import LanguageModel
from infrastructure.dtos.sql_alchemy_models.base import Base


class SQLAlchemyPersistenceDataSource(PersistanceDataSource):
    def __init__(self):

        SQLALCHEMY_DATABASE_URL = "postgresql://admin:password@db_server/translator_db"  # PostgreSQL URL

        # For SQLite, you can use: "sqlite:///./test.db" instead of PostgreSQL

        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)  # for SQLite add check_same_thread=False
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_conferences(self) -> List[ConferenceModel]:
        """
        Retrieve all conferences from the database.
        """
        conferences = self.query(ConferenceModel).all()
        return [self._map_to_dto(conference) for conference in conferences]
    
    def add_new_conference(self, conference: ConferenceModel) -> None:
        """
        Add a new conference to the database.
        """
        self.add(conference)
        self.commit()

    def update_conference(self, conference_id: str, new_name: str) -> bool:
        """
        Update a conference's name based on the conference ID.
        """
        # conference = self.query(Conference).filter_by(id=conference_id).first()
        # if conference:
        #     conference.name = new_name
        #     self.commit()
        #     return True
        # return False
        pass

    def delete_conference(self, conference_id: str) -> bool:
        """
        Delete a conference based on the conference ID.
        """
        # conference = self.query(Conference).filter_by(id=conference_id).first()
        # if conference:
        #     self.delete(conference)
        #     self.commit()
        #     return True
        # return False
        pass

    def add_user(self, user: UserModel) -> None:
        """
        Add a user to a specific conference.
        """
        self.session.add(user)
        self.session.commit()

    def get_users(self, conference_id: str) -> List[UserModel]:
        """
        Retrieve all users (attendees) for a specific conference.
        """
        # conference = self.query(Conference).filter_by(id=conference_id).first()
        # if conference:
        #     return conference.attendees
        return []

    def update_user(self, user_id: str, new_name: str) -> bool:
        """
        Update a user's name based on the user ID.
        """
        # user = self.query(User).filter_by(id=user_id).first()
        # if user:
        #     user.name = new_name
        #     self.commit()
        #     return True
        return False

    def delete_user(self, user_id: str) -> bool:
        """
        Remove a user from the database.
        """
        # user = self.query(User).filter_by(id=user_id).first()
        # if user:
        #     self.delete(user)
        #     self.commit()
        #     return True
        return False

    def add_user_to_conference(self, attendance: AttendanceModel) -> None:
        """
        Add a user to a conference, with the user's language and conference details.
        """
        user = self.query(UserModel).filter_by(id=attendance.user_id).first()
        conference = self.query(ConferenceModel).filter_by(id=attendance.conference_id).first()
        if user and conference:
            # Add user as an attendee with a language
            self.session.add(attendance)
            self.session.commit()

    def get_attendees_for_conference(self, conference_id: str) -> List[AttendanceModel]:
        """
        Get all attendees for a specific conference.
        """
        # conference = self.query(Conference).filter_by(id=conference_id).first()
        # if conference:
        #     return conference.attendees
        return []

    def exit_user_from_conference(self, user_id: str, conference_id: str) -> bool:
        """
        Remove a user from a specific conference.
        """
        # attendance = self.query(ConferenceAttendance).filter_by(user_id=user_id, conference_id=conference_id).first()
        # if attendance:
        #     self.delete(attendance)
        #     session.commit()
        #     return True
        return False

    def update_user_in_conference(self, user_id: str, conference_id: str, new_language: LanguageModel) -> bool:
        """
        Update a user's language in a conference.
        """
        # attendance = session.query(ConferenceAttendance).filter_by(user_id=user_id, conference_id=conference_id).first()
        # if attendance:
        #     attendance.language_id = new_language.id
        #     session.commit()
        #     return True
        return False
    


    def add_language(self, language: LanguageModel) -> None:
        """
        Add a user to a specific conference.
        """
        self.session.add(language)
        self.session.commit()
        pass
    
    def delete_language(self, language: LanguageModel) -> None:
        """
        Add a user to a specific conference.
        """
        self.session.delete(language)
        self.session.commit()
        pass
    
    def get_languages(self) -> list[LanguageModel]:
        """
        Add a user to a specific conference.
        """
        langs = self.session.query(LanguageModel).all()
        pass

    def migrate_db(self) -> bool:
        """
        delete and recreate translator_db.
        """
        Base.metadata.create_all(bind=self.engine)
        
