import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from infrastructure.dtos.sql_alchemy_models.base import Base


class LanguageModel(Base):
    __tablename__ = 'languages'
    
    # Use UUID for the id and auto-generate it with uuid.uuid4
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Other columns
    name = Column(String, nullable=False)
    translation_id = Column(String, nullable=False)
    t2t = Column(Boolean, nullable=False)
    asr = Column(Boolean, nullable=False)
    tts = Column(Boolean, nullable=False)
  
    
    def __repr__(self):
        return f"Language(id={self.id}, name={self.name})"

