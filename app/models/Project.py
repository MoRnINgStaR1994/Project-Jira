from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from ..dbengine import engine

Base = declarative_base()


@dataclass
class Project(Base):
    __tablename__ = 'projects'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    user_id: int = Column(Integer, ForeignKey('persons.id'), nullable=False)
    description: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)


Base.metadata.create_all(engine)
