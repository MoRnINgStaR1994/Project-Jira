from sqlalchemy import (
    Column,
    Integer,
    JSON,
    String

)
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from ..dbengine import engine

Base = declarative_base()


@dataclass
class Board(Base):
    __tablename__ = 'boards'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
    project_id: int = Column(Integer, nullable=False)
    board_columns: list = Column(JSON, nullable=False, default=['todo', 'in_progress', 'on_hold', 'preview', 'failed', 'done'])


Base.metadata.create_all(engine)

