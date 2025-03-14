from fastapi import APIRouter, Depends
from ..schemas.project import ProjectEditDTO, ProjectCreateDTO, BoardCreateDTO, BoardEditDTO
from ..services import ProjectService
from ..utils import get_current_user

router = APIRouter(prefix="/project", tags=["Projects"])

# PROJECT ENDPOINTS


@router.post("/create")
async def create_project(data: ProjectCreateDTO, user: dict = Depends(get_current_user)):
    return ProjectService.create_project(data, user['id'])


@router.get("/")
async def list_project(user: dict = Depends(get_current_user)):
    return ProjectService.list_project(user['id'])


@router.get("/details/{id}")
async def project_details(id: int, user: dict = Depends(get_current_user)):
    return ProjectService.project_details(id, user)


@router.post("/edit/{id}")
async def edit_project(id: int, details: ProjectEditDTO, user: dict = Depends(get_current_user)):
    return ProjectService.edit_project(id, details, user['id'])


@router.delete("/delete/{id}")
async def delete_project(id: int, user: dict = Depends(get_current_user)):
    return ProjectService.delete_project(id, user)


# BOARD ENDPOINTS
@router.post("/board/create")
async def create_board(data: BoardCreateDTO, user: dict = Depends(get_current_user)):
    return ProjectService.create_board(data, user)


@router.get("/board/details/{id}")
async def board_details(id: int, user: dict = Depends(get_current_user)):
    return ProjectService.board_details(id, user)


@router.post("/board/edit/{id}")
async def edit_board(id: int, data: BoardEditDTO):
    return ProjectService.edit_board(id, data)


@router.delete("/board/delete/{id}")
async def delete_board(id: int,user: dict = Depends(get_current_user)):
    return ProjectService.delete_board(id, user)

