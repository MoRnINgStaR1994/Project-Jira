from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from ..dbengine import engine

Base = declarative_base()


@dataclass
class Person(Base):
    __tablename__ = 'persons'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String, nullable=True)
    password: str = Column(String, nullable=True)
    email: str = Column(String(50), unique=True, nullable=False)
    is_verified: bool = Column(Boolean, default=False)


Base.metadata.create_all(engine)
