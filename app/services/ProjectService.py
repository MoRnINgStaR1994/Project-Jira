import json.encoder

from fastapi import HTTPException, status

from ..schemas.project import ProjectCreateDTO, ProjectEditDTO, BoardCreateDTO, BoardEditDTO
from ..models.Project import Project
from ..models.Board import Board
from ..repositories.ProjectRepository import insert_new_project, list_user_projects, get_project_owner, \
    delete_user_project, create_project_board, delete_project_board, get_project_id, get_project_details, list_boards, \
    get_board_details, get_board_tickets, update_project, get_board_by_id, update_board


def create_project(data: ProjectCreateDTO, user_id: int) -> Project:
    project = Project(name=data.name, description=data.description, is_active=True, user_id=user_id)
    insert_new_project(project)

    return project


def edit_project(project_id: int, details: ProjectEditDTO, user_id: int) -> bool:
    # Fetch the existing project
    owner = get_project_owner(project_id)

    if not owner or owner != user_id:
        raise Exception("Project not found or not accessible")

    # Save updates to the database
    update_project(details, project_id)

    return True


def delete_project(id: int, user: dict) -> bool:
    owner = get_project_owner(id)
    print(owner)
    print(user)
    if not owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='model not found')
    elif owner != user['id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='request is forbidden')

    return delete_user_project(id)


def list_project(user_id: int) -> list[Project]:
    projects = list_user_projects(user_id)

    return projects


def project_details(id: int, user: dict) -> Project:
    details = get_project_details(id, user['id'])
    if not details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='model not found')

    boards = list_boards(id)
    details['boards'] = boards

    return details


def board_belongs_to_user(id: int, user_id: int) -> bool:
    project_id = get_project_id(id)

    if not project_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='model not found')

    owner = get_project_owner(project_id)

    if not owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='model not found')

    return owner == user_id


def board_details(id: int, user: dict) -> Board:
    if not board_belongs_to_user(id, user['id']):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='request is forbidden')

    print(id)

    board = get_board_details(id)
    board['tickets'] = get_board_tickets(id)

    return board


def create_board(data: BoardCreateDTO, user: dict) -> Board:
    owner = get_project_owner(data.project_id)
    if not owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='model not found')
    elif owner != user['id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='request is forbidden')

    board = Board(name=data.name, project_id=data.project_id, board_columns=json.dumps(data.board_columns))

    create_project_board(board)

    return board


def edit_board(id: int, data: BoardEditDTO) -> Board:
    # Fetch the existing board
    board = get_board_by_id(id)

    if not board:
        raise Exception("Board not found")

    # Update only the provided fields
    updated_data = {
        "name": data.name if data.name is not None else board["name"],
        "board_columns": data.board_columns if data.board_columns is not None else board["board_columns"],
    }

    # Save updates to the database
    update_board(id, updated_data)

    # Update the board object for the response
    board["name"] = updated_data["name"]
    board["board_columns"] = updated_data["board_columns"]

    return board


def delete_board(id: int, user: dict) -> bool:
    if not board_belongs_to_user(id, user['id']):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='request is forbidden')

    delete_project_board(id)
    return True
