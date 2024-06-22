from fastapi import APIRouter

orders = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


# See All Orders Now
@orders.get("/")
def get_orders():
    return {"orders": "orders"}


# Place Order
@orders.post("/place")
def place_order():
    return {"data": "order_placed"}


# To Update Some Info About Order
@orders.patch("/update/{id}")
def update_order(id: str):
    return {"data": "order_updated"}


@orders.delete("/delete/{id}")
def delete_order(id: str):
    return {"data": "order_deleted"}
