from fastapi import FastAPI
from db import models
from db.config import engine
from routes import orders


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Market FastAPI',
)

app.include_router(orders.orders)
