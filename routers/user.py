from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

import cruds.user as crud
from routers.db import get_db
import schemas.user as schema

router = APIRouter(prefix="/user")


@router.get("/", response_model=List[schema.User])
async def list(db: Session = Depends(get_db)):
    return crud.list(db)


@router.get("/{id}", response_model=schema.User)
async def get(id: int, db: Session = Depends(get_db)):
    user = crud.get(db, id)
    if user is None:
        raise HTTPException(404)
    return user


@router.post("/", response_model=schema.User)
async def create(user: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.create(db, user)


@router.put("/{id}", response_model=schema.User)
async def update(id: int, user: schema.User, db: Session = Depends(get_db)):
    user = crud.update(db, id, user)
    if user is None:
        raise HTTPException(404)
    return user


@router.delete("/{id}", response_model=schema.User)
async def delete(id: int, db: Session = Depends(get_db)):
    user = crud.delete(db, id)
    if user is None:
        raise HTTPException(404)
    return user
