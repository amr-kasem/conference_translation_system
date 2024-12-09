import uuid
from sqlalchemy import  Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from infrastructure.dtos.sql_alchemy_models.base import Base

class UserModel(Base):
    __tablename__ = 'users'
    
    # Auto-generated UUID for the 'id' field
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Other fields
    name = Column(String, nullable=False)
    home_language_id = Column(UUID(as_uuid=True), ForeignKey('languages.id'), nullable=True)
    
    # Relationships
    home_language = relationship('LanguageModel')
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, home_language_id={self.home_language_id})"

