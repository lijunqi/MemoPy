from typing import Optional
from pydantic import BaseModel, Field


class MyItem(BaseModel):
    name: str
    description: Optional[str] = Field(
        default=None,
        description="An optional description of the item",
    )
    #description: str | None = None
    price: float = Field(description="Price is required!!!")
    tax: float = Field(default=1.23)
