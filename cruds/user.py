from typing import List

from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models.user as model
import schemas.user as schema

bcrypt_context = CryptContext(schemes=["bcrypt"])


def list(db: Session) -> List[model.User]:
    return db.query(model.User).all()


def get(db: Session, id: int) -> model.User:
    return db.query(model.User).filter(model.User.id == id).first()


def create(db: Session, user: schema.UserCreate) -> model.User:
    user = model.User(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=get_hashed_password(user.password),
        is_active=user.is_active,
    )
    db.add(user)
    db.commit()
    db.flush(user)
    return user


def update(db: Session, id: int, new_user: schema.User) -> model.User:
    user = db.query(model.User).filter(model.User.id == id).first()
    if user is None:
        return None
    user.title = new_user.title
    user.description = new_user.description
    user.priority = new_user.priority
    user.complete = new_user.complete
    db.commit()
    db.flush(user)
    return user


def delete(db: Session, id: int) -> model.User:
    user = db.query(model.User).filter(model.User.id == id).first()
    if user is None:
        return None
    db.delete(user)
    db.commit()
    db.flush(user)
    return user


def get_hashed_password(password) -> str:
    return bcrypt_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db: Session):
    user = db.query(model.User).filter(model.User.username == username).first()
    if user is None:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
