from pydantic import BaseModel

class Base(BaseModel):
    id: int
    name: str


class A(Base):
    age: int

a = A(id=1, name="Tom", age=10)
print("a: ", a)
print("a.model_dump(): ", a.model_dump())
