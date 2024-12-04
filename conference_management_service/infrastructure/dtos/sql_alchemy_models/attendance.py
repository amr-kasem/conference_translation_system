from sqlalchemy import  Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from infrastructure.dtos.sql_alchemy_models.base import Base

class AttendanceModel(Base):
    __tablename__ = 'conference_attendances'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    conference_id = Column(String, ForeignKey('conferences.id'))
    language_id = Column(String, ForeignKey('languages.id'))
    start = Column(DateTime)
    end = Column(DateTime)
    user = relationship('UserModel')
    language = relationship('LanguageModel')
    
    def __repr__(self):
        return f"ConferenceAttendance(user_id={self.user_id}, conference_id={self.conference_id}, language={self.language.name})"
