import uuid

from sqlalchemy import  Column, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from infrastructure.dtos.sql_alchemy_models.base import Base


class ConferenceModel(Base):
    __tablename__ = 'conferences'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    private = Column(Boolean)
    start = Column(DateTime)
    end = Column(DateTime)
    
    speaker_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    speaker = relationship('UserModel')
    
    attendees = relationship('AttendanceModel')


    
    def __repr__(self):
        return f"Conference(id={self.id}, name={self.name})"