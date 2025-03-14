from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from ..dbengine import engine

Base = declarative_base()

@dataclass
class Ticket(Base):
    __tablename__ = 'tickets'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    estimation: int = Column(Integer, nullable=False, default=0)
    priority: int = Column(Integer, nullable=False, default=0)
    status: str = Column(String, nullable=False, default='todo')
    board_id: int = Column(Integer, ForeignKey('boards.id'), nullable=False)


Base.metadata.create_all(engine)
