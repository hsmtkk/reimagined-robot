from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

import cruds.address as crud
from routers.db import get_db
from routers.token import get_current_user, get_user_exception
import schemas.address as schema

router = APIRouter(prefix="/address")


@router.post("/")
async def create(
    address: schema.Address,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()
    return crud.create(db, address, user)
