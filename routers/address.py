from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.address as crud
from routers.db import get_db
from routers.token import get_current_user, get_user_exception
import schemas.address as schema

router = APIRouter(prefix="/address")


@router.post("/", response_model=schema.Address)
async def create(
    address: schema.AddressCreate,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()
    return crud.create(db, address, user)
