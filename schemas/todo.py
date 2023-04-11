from typing import Optional

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6)
    complete: bool

    class Config:
        orm_mode = True


class Todo(TodoCreate):
    id: int
