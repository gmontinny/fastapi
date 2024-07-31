from sqlalchemy.orm import Session
from pydantic import EmailStr

import models


def get_user(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: models.User):
    db_user = models.User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_token(db: Session, token: str):
    return db.query(models.Token).filter(models.Token.token == token).first()

def create_token(db: Session, token: str, user_id: int):
    db_token = models.Token(token=token, user_id=user_id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token