from pydantic import BaseModel
from typing import Optional


class ProjectCreateDTO(BaseModel):
    name: str
    description: str


class ProjectEditDTO(BaseModel):
    name: str = None
    description: str = None
    is_active: bool = None


class BoardCreateDTO(BaseModel):
    project_id: int
    name: str
    board_columns: Optional[list] = ['todo', 'in_progress', 'on_hold', 'preview', 'failed', 'done']


class BoardEditDTO(BaseModel):
    name: Optional[str] = None
    board_columns: Optional[list] = None

