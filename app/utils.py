from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import JWT, jwk_from_pem, exceptions
import hashlib
from datetime import datetime, timedelta, timezone
from jwt.utils import get_int_from_datetime

jwt = JWT()



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_jwt(id, email, isRefresh=False):
    payload = {
        "id": id,
        "email": email,
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(datetime.now(timezone.utc) + timedelta(minutes=30)),
    }

    if isRefresh:
        payload['exp'] = get_int_from_datetime(datetime.now(timezone.utc) + timedelta(hours=2))

    with open('/Users/macbookpro/PycharmProjects/Project Jira/app/rsa_private_key.pem', 'rb') as fh:
        signing_key = jwk_from_pem(fh.read())
        return jwt.encode(payload, signing_key, alg='RS256')


def verify_jwt(token):
    try:
        with open('/Users/macbookpro/PycharmProjects/Project Jira/app/rsa_public_key.pem', 'rb') as fh:
            verifying_key = jwk_from_pem(fh.read())

            decoded = jwt.decode(token, verifying_key, do_time_check=True)
        return decoded
    except exceptions.JWTException:
        return {"error": "Invalid token"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = verify_jwt(token)
    if not payload or 'error' in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload  # Return the user information

