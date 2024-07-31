from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
from crud import get_user, create_user
from db import *
from schemas import GetUser, PostUser, LoginUser
from datetime import date, datetime, timedelta, time

from utils.auth import create_access_token, create_refresh_token, JWTBearer, decodeJWT

route = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2bearer = OAuth2PasswordBearer(tokenUrl='auth/login')


def get_user_by_id(user_id: int, db: Session) -> models.User:
    """
    Get a user by ID
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_current_user(token: str = Depends(JWTBearer())) -> models.User:
    """
    Get current user from JWT token
    """
    payload = decodeJWT(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token",
        )
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token",
        )
    # Assuming you have a function to get user by id from the database
    user = get_user_by_id(user_id)  # Implement this function
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user

# Register new user using email, username, password
@route.post("/register", response_model=GetUser)
def register_user(payload: PostUser, db: Session = Depends(get_db)):
    if not payload.email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please add Email",
        )
    user = get_user(db, payload.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User with email {payload.email} already exists",
        )
    user = create_user(db, payload)
    print(user)

    return user


@route.post("/login")
def login_user(payload: LoginUser, db: Session = Depends(get_db)):
    """
    Login user based on email and password
    """
    if not payload.email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please add Phone number",
        )

    user = get_user(db, payload.email)
    token = create_access_token(user.id, timedelta(minutes=30))
    refresh = create_refresh_token(user.id, timedelta(minutes=1008))

    return {'access_token': token, 'token_type': 'bearer', 'refresh_token': refresh, "user_id": user.id}
