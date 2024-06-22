from fastapi import APIRouter
from db import schemas, models

users = APIRouter(
    prefix="/users",
    tags=["users"],
)


@users.post('/create')
def create_user(request):
    pass
