from functools import cached_property
from pydantic import BaseModel, computed_field, Field

class Circle(BaseModel):
    center: tuple[int, int] = (0, 0)
    radius: int = Field(default=1, gt=0, frozen=True)

    @computed_field
    @cached_property
    def area(self) -> float:
        print("Calculating area ...")
        return 3.14 * self.radius**2


c = Circle()
print("c = ", c) # only call area once
print("area = ", c.area) # ! do not calculate again
print("area = ", c.area)
print("area = ", c.area)

#c.radius = 5
#print("c = ", c)
#print("area = ", c.area)
