from pydantic import BaseModel, Field


class MyItem(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(description="Price is required!!!")
    tax: float = Field(default=1.23)
