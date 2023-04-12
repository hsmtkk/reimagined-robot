from typing import Optional

from pydantic import BaseModel, Field


class AddressCreate(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    postalcode: str

    class Config:
        orm_mode = True


class Address(AddressCreate):
    id: int
