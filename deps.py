from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from auth.utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

from jose import jwt
from pydantic import ValidationError
from models.TokenPayload import TokenPayload
from DataBase.DBDeclaration import GodSlaveModel
from fastapi import Cookie
from DataBase.DBget import db



async def get_current_user(auth_token: str | None = Cookie(default=None)):
    try:
        payload = jwt.decode(
            auth_token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user: Union[dict[str, Any], None] = db.query(GodSlaveModel).filter(GodSlaveModel.login==token_data.sub).first()
    print(user)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return user
