"""
The @overload-decorated definitions are for the benefit of the type checker only,
since they will be overwritten by the non-@overload-decorated definition,
while the latter is used at runtime but should be ignored by a type checker.
"""

from typing import overload

# * ONLY for type checker
@overload
def process(response: None) -> None:
    ...

@overload
def process(response: int) -> tuple[int, str]:
    ...

@overload
def process(response: bytes) -> str:
    ...

# * Be ignored by type checker
def process(response):
    # actual implementation goes here
    return response

response = None
print("1. This is response: ", process(response))

response = 123
print("2. This is response: ", process(response))

response = b"asdf"
print("3. This is response: ", process(response))

response = [1,2,3]
print("4. This is response: ", process(response))


from pydantic import BaseModel

class A(BaseModel):
    name: str
    age: int

class C(BaseModel):
    name: str
    age: int
class B(A):
    number: int
    description: str

@overload
def do_work(item: A) -> None:
    ...

@overload
def do_work(item: B) -> None:
    print(item)

def do_work(item):
    if type(item) == A:
        print("This is A item: ", item.name)
    elif type(item) == B:
        print("This is B item: ", item.name)
    else:
        print("This is ? item: ", item)

a = A(name="Tom", age=123)
do_work(a)
b = B(name="Jerry", age=11, number=22, description="This is Jerry")
do_work(b)

do_work("???")


class Duck:

    @overload
    def quack(self) -> None: ...

    @overload
    def quack(self, mark: str) -> None: ...

    # 以上两个方法最终会被这个方法覆盖掉
    def quack(self, arg=None):
        if arg:
            print(f"GaGaGa: {arg}")
        else:
            print("GaGaGa!")

d = Duck()
d.quack()                   # Output: GaGaGa!
d.quack("This is a duck~")  # Output: GaGaGa: This is a duck~
