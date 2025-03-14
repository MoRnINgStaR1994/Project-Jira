from fastapi import HTTPException
from starlette import status

from ..schemas.ticket import TicketCreateDTO, TicketEditDTO
from ..models.Ticket import Ticket
from ..repositories.TicketRepository import insert_new_ticket, delete_project_board_ticket, get_ticket_owner, \
    get_ticket_details, get_ticket_by_id, update_ticket


def ticket_belongs_to_user(id: int, user_id: int) -> bool:
    owner = get_ticket_owner(id)
    if not owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='model not found')

    return owner == user_id


def create_ticket(data: TicketCreateDTO) -> Ticket:
    ticket = Ticket(title=data.title, description=data.description, estimation=data.estimation, priority=data.priority,
                    status=data.status, board_id=data.board_id)

    insert_new_ticket(ticket)

    return ticket


def delete_ticket(id: int, user: dict) -> bool:
    is_owner = ticket_belongs_to_user(id, user['id'])

    if not is_owner:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Access Denied')

    return delete_project_board_ticket(id)


def ticket_details(id: int, user: dict) -> Ticket:
    ticket_owner = ticket_belongs_to_user(id, user['id'])

    if not ticket_owner:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Access Denied')

    return get_ticket_details(id)


def edit_ticket(ticket_id: int, details: TicketEditDTO, user_id: int) -> dict:
    # Ensure the ticket belongs to the user
    if not ticket_belongs_to_user(ticket_id, user_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Request is forbidden")

    # Fetch the existing ticket
    existing_ticket = get_ticket_by_id(ticket_id)
    if not existing_ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

    # Update only the provided fields
    updated_data = {
        "title": details.title if details.title is not None else existing_ticket["title"],
        "description": details.description if details.description is not None else existing_ticket["description"],
        "estimation": details.estimation if details.estimation is not None else existing_ticket["estimation"],
        "priority": details.priority if details.priority is not None else existing_ticket["priority"],
        "status": details.status if details.status is not None else existing_ticket["status"],
    }

    # Save the updates
    if not update_ticket(ticket_id, updated_data):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update the ticket")

    # Return the updated ticket
    updated_ticket = get_ticket_by_id(ticket_id)
    return updated_ticket

