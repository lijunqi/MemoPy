
from typing import Any


class MyClass:
    def __init__(self, x=0) -> None:
        print("initializing...")
        self.counter = x
    
    # * def __call__(self, *args: Any, **kwds: Any) -> Any:
    def __call__(self, x=1) -> Any:
        print("updating counter...")
        self.counter += x

a = MyClass()
print("counter = ", a.counter) # 0

a()
print("counter = ", a.counter) # 1

a(123)
print("counter = ", a.counter) # 124

MyClass.__call__(a, 2)
print("counter = ", a.counter) # 126
