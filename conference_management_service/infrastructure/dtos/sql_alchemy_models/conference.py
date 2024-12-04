from sqlalchemy import create_engine, Column, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from infrastructure.dtos.sql_alchemy_models.base import Base


class ConferenceModel(Base):
    __tablename__ = 'conferences'
    
    id = Column(String, primary_key=True)
    name = Column(String)
    private = Column(Boolean)
    start = Column(DateTime)
    end = Column(DateTime)
    
    speaker_id = Column(String, ForeignKey('users.id'))
    speaker = relationship('UserModel')
    
    attendees = relationship('AttendanceModel')


    
    def __repr__(self):
        return f"Conference(id={self.id}, name={self.name})"