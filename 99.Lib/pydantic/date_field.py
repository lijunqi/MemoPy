
from datetime import datetime, timezone
from pydantic import BaseModel, AwareDatetime

class Model(BaseModel):
    t: AwareDatetime

t1 = datetime.now(timezone.utc)
print("t1: ", t1)
t1_str = t1.replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")
print("t1_str: ", t1_str)

m1 = Model(t=t1)
print("m1: ", m1)
print("m1.model_dump(): ", m1.model_dump())


class Foo(BaseModel):
    data: str = "Some data"
    created_at: datetime = datetime.now()

f1 = Foo()
f2 = Foo()
print("f1: ", f1)
print("f2: ", f2)
print("f1.created_at == f2.created_at ", f1.created_at == f2.created_at)