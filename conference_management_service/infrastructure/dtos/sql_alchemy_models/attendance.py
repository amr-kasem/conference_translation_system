import uuid

from sqlalchemy import  Column,  ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from infrastructure.dtos.sql_alchemy_models.base import Base

class AttendanceModel(Base):
    __tablename__ = 'conference_attendances'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    conference_id = Column(UUID(as_uuid=True), ForeignKey('conferences.id'))
    language_id = Column(UUID(as_uuid=True), ForeignKey('languages.id'))
    start = Column(DateTime)
    end = Column(DateTime)
    user = relationship('UserModel')
    language = relationship('LanguageModel')
    
    def __repr__(self):
        return f"ConferenceAttendance(user_id={self.user_id}, conference_id={self.conference_id}, language={self.language.name})"
