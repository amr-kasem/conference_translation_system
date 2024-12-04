from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from infrastructure.dtos.sql_alchemy_models.base import Base


class ConferenceLanguage(Base):
    __tablename__ = 'conference_languages'
    
    conference_id = Column(String, ForeignKey('conferences.id'), primary_key=True)
    language_id = Column(String, ForeignKey('languages.id'), primary_key=True)
