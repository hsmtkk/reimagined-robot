from typing import List

from sqlalchemy.orm import Session

import models.address
import models.user
import schemas.address


def create(
    db: Session, address: schemas.address.AddressCreate, user: dict
) -> models.address.Address:
    new_address = models.address.Address(
        address1=address.address1,
        address2=address.address2,
        city=address.city,
        state=address.state,
        country=address.country,
        postalcode=address.postalcode,
    )
    db.add(new_address)
    db.flush()

    new_user = (
        db.query(models.user.User).filter(models.user.User.id == user["id"]).first()
    )
    new_user.address_id = new_address.id
    db.add(new_user)

    db.commit()
    return new_address
