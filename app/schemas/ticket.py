from pydantic import BaseModel
from typing import Optional


class TicketCreateDTO(BaseModel):
    board_id: int
    title: str
    description: str
    estimation: int
    priority: int
    status: str


class TicketEditDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    estimation: Optional[int] = None
    priority: Optional[int] = None
    status: Optional[str] = None

