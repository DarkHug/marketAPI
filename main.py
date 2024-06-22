from fastapi import FastAPI
from db import models
from db import config
from routes import orders, sellers


models.Base.metadata.create_all(bind=config.engine)

app = FastAPI(
    title='Market FastAPI',
)

app.include_router(orders.orders)
app.include_router(sellers.sellers)
