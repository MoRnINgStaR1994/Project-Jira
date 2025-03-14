from fastapi import HTTPException
from starlette import status

from ..models.Person import Person
from ..schemas.person import PersonRegisterDTO, PersonLoginDTO
from ..repositories.PersonRepository import create_user, authenticate_user
from ..utils import generate_jwt, verify_jwt


def register_user(schema: PersonRegisterDTO) -> Person:
    user = Person(username=schema.username, password=schema.password, email=schema.email, is_verified=True)

    user_created = create_user(username=schema.username, password=schema.password, email=schema.email, is_verified=True)

    if user_created:
        # send email notification
        pass
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')

    return user


def login_user(credentials: PersonLoginDTO) -> dict[str, str]:
    result = authenticate_user(credentials.email, credentials.password)
    print(result)
    if result:
        return {
            "accessToken": generate_jwt(result[0], result[1]),
            "refreshToken": generate_jwt(result[0], result[1], True)
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='email or password is incorrect')


def renew_access_token(token: str):
    payload = verify_jwt(token)
    print(payload)
    return {
        "accessToken": generate_jwt(payload['id'], payload['email'])
    }