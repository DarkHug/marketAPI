from typing import List, Optional, Generic
from pydantic import BaseModel
from pydantic.generics import GenericModel


class Seller(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "first_name": "Almas",
                "last_name": "Muratov",
                "email": "example@example.com",
                "password": "<PASSWORD>",
            }
        }
