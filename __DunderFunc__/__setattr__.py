"""
每次类实例进行属性赋值时都会调用__setattr__()
"""

from typing import Any


class User:
    def __init__(self, name, age) -> None:
        print("    Construct name")
        self.name = name
        print("    Construct age")
        self.age = age
        print("    Construct Done")
    
    def __setattr__(self, k: str, v: Any) -> None:
        print("====== In setattr ======: ", k, v)

print("[Begin] Construct")
u = User("Tom", 123)
print("[End] Construct")

print("[Begin] Change name")
u.name = "Jerry"
print("[End] Change name")

print("[Begin] Change age")
u.age = 456
print("[End] Change age")
