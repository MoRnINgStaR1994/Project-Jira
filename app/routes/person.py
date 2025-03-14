from fastapi import APIRouter
from ..schemas.person import PersonRegisterDTO, PersonLoginDTO, RenewAccessToken
from ..services.PersonService import register_user, login_user, renew_access_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
async def register(user: PersonRegisterDTO):
    return register_user(user)


@router.post("/login")
async def login(user: PersonLoginDTO):
    return login_user(user)


@router.post("/refresh")
async def get_new_access_token(data: RenewAccessToken):
    return renew_access_token(data.refreshToken)
