from fastapi import APIRouter, Depends
from ..services import TicketService
from ..utils import get_current_user
from ..schemas.ticket import TicketCreateDTO, TicketEditDTO

router = APIRouter(prefix="/ticket", tags=["Ticket"])

# TICKET ENDPOINTS

@router.post("/create")
async def create(data: TicketCreateDTO,):
    return TicketService.create_ticket(data)


@router.get("/details/{id}")
async def details(id: int, user: dict = Depends(get_current_user)):
    return TicketService.ticket_details(id, user)


@router.post("/edit/{id}")
async def edit_ticket(id: int, data: TicketEditDTO, user: dict = Depends(get_current_user)):
    return TicketService.edit_ticket(id, data, user["id"])


@router.delete("/delete/{id}")
async def delete(id: int, user: dict = Depends(get_current_user)):
    return TicketService.delete_ticket(id, user)


