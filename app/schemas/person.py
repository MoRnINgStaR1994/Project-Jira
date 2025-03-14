from pydantic import BaseModel

class PersonRegisterDTO(BaseModel):
    username: str
    password: str
    email: str


class PersonLoginDTO(BaseModel):
    email: str
    password: str


class RenewAccessToken(BaseModel):
    refreshToken: str
