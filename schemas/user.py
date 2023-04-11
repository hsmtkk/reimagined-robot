from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    is_active: bool

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
