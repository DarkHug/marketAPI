from fastapi import APIRouter, Depends, status
from db import schemas, models, config
from sqlalchemy.orm import Session

sellers = APIRouter(
    prefix="/seller",
    tags=["Seller"],
)

get_db = config.get_db


@sellers.post('/create', response_model=models.Sellers, status_code=status.HTTP_201_CREATED)
def register_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    new_seller = models.Sellers(first_name=request.first_name, last_name=request.last_name)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
