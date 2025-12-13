import time
from datetime import datetime, timezone
from pydantic import BaseModel, Field, AwareDatetime, field_validator

class DateModel(BaseModel):
    t: AwareDatetime = Field(default_factory=datetime.now)

now1 = datetime.now(timezone.utc)
print("now1: ", now1)
now1_str = now1.replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")
print("now1_str: ", now1_str)

dm1 = DateModel(t=now1)
print("dm1: ", dm1)
print("dm1.t: ", dm1.t, type(dm1.t))
print("dm1.model_dump(): ", dm1.model_dump())
now2 = datetime.now(timezone.utc)
print("now2 > dm1.t --- ", now2 > dm1.t)

dm2 = DateModel()
time.sleep(1)
dm3 = DateModel()
if dm2.t != dm3.t:
    print("dm2 != dm3")
print()


# * Custom parsing
class CustomDate(BaseModel):
    t: datetime

    @field_validator("t")
    @classmethod
    def validate_date(cls, v: str) -> datetime:
        return datetime.strptime(v, "%Y-%m-%dT%H:%M%S").replace(tzinfo=timezone.utc)

cd1 = CustomDate(t="2025-01-01T01:02:03")


class Foo(BaseModel):
    created_at: datetime = datetime.now() # ❌ Calculate when compile (value never change)

f1 = Foo()
time.sleep(1)
f2 = Foo()
print("f1: ", f1)
print("f2: ", f2)
print("f1.created_at == f2.created_at ", f1.created_at == f2.created_at)

class Bar(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now) # ✅

b1 = Bar()
time.sleep(1)
b2 = Bar()
print("b1: ", b1)
print("b2: ", b2)
print("b1.created_at == b2.created_at ", b1.created_at == b2.created_at)
