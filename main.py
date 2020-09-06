from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def index():
    return {"Welcome": "FastAPI Example"}


@app.post("/items/")
def accept_item(item: Item):
    return {"item_name": item.name, "price": item.price}



