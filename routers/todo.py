from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

import cruds.todo as crud
from routers.db import get_db
from routers.token import get_current_user, get_user_exception
import schemas.todo as schema

router = APIRouter(prefix="/todo")


@router.get("/", response_model=List[schema.Todo])
async def list(db: Session = Depends(get_db)):
    return crud.list(db)


@router.get("/{id}", response_model=schema.Todo)
async def get(id: int, db: Session = Depends(get_db)):
    todo = crud.get(db, id)
    if todo is None:
        raise HTTPException(404)
    return todo


@router.post("/", response_model=schema.Todo)
async def create(todo: schema.TodoCreate, db: Session = Depends(get_db)):
    return crud.create(db, todo)


@router.put("/{id}", response_model=schema.Todo)
async def update(id: int, todo: schema.Todo, db: Session = Depends(get_db)):
    todo = crud.update(db, id, todo)
    if todo is None:
        raise HTTPException(404)
    return todo


@router.delete("/{id}", response_model=schema.Todo)
async def delete(id: int, db: Session = Depends(get_db)):
    todo = crud.delete(db, id)
    if todo is None:
        raise HTTPException(404)
    return todo
