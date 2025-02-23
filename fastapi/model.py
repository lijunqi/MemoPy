from pydantic import BaseModel


class MyItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
