import datetime
import time

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from passlib.exc import UnknownHashError

from models.jwt_users import JWTUser
from utils.consts import (
    JWT_EXPIRATION_TIME_MINUTE,
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
)

pwd_context = CryptContext(schemes=["bcrypt"])
jwt_user1 = {
    "username": "user1",
    "password": "$2b$12$Gpewk6paEw8Np9Un4xE6O.XM8uMH/hJLuKhs.rljFTI2VemEU6/ee",
    "disabled": False,
    "role": "admin",
}
fake_jwt_user1 = JWTUser(**jwt_user1)
jwt_user_fake_db = [{}]
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except UnknownHashError:
        return False


def authenticate_user(user: JWTUser):
    if fake_jwt_user1.username == user.username:
        if verify_password(user.password, fake_jwt_user1.password):
            user.role = "admin"
            return user
    return None


def create_jwt_token(user: JWTUser):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=JWT_EXPIRATION_TIME_MINUTE
    )
    jwt_payload = {"sub": user.username, "exp": expiration, "role": user.role}
    jwt_token = jwt.encode(
        jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM
    )
    return jwt_token


def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM
        )
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        if time.time() < expiration:
            if fake_jwt_user1.username == username:
                return final_checks(role)
    except Exception as e:
        return False
    return False


def final_checks(role: str):
    if role == "admin":
        return True
    return False
