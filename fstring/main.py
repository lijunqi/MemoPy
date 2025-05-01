
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"[str ] User name is {self.name}, age is {self.age}"

    def __repr__(self) -> str:
        return f"[repr] User {self.name} is {self.age} years old."

u = User("Tom", 123)
print(f"User     : {u}")
print(f"User str : {u!s}")
print(f"User repr: {u!r}")


x = 'A'
print(f"A (ascii): {x!a}")
print(f"A (str  ): {x!s}")
print(f"A (repr ): {x!r}")

name = "Jacky"
print(f"Name is (ascii): {name!a}")
print(f"Name is (str  ): {name!s}")
print(f"Name is (repr ): {name!r}")

n = 123
print(f"n = (ascii): {n!a}")
print(f"n = (str  ): {n!s}")
print(f"n = (repr ): {n!r}")

score = 99.123456789
print(f"Score str : {score}")
print(f"Score repr: {score!r}")


# * Use "=" to padding total 51 characters
print(f"{'Tip 1':=^51}")
n: int = 1_000_000_000
print("n = ", n)
print(f"n = {n:_}")
print(f"n = {n:,}")


print(f"{'Tip 2':=^51}")
d = {
    "name": "Tom",
    "age" : 12,
    "email": "Tom@gmail.com"
}
for k, v in d.items():
    print(f"{k:5}: {v:>20}") # left align, righ align
var = "var"
print(f"{var:^10}:") # center align

print(f"{'Tip 3':=^51}")
print(f"{var:_>10}")
print(f"{var:#<10}")
print(f"{var:|^10}")
print(f"{var:=^10}")

print(f"{'Tip 4':=^51}")
from datetime import datetime
now = datetime.now()
print(f"Date Now : {now:%Y-%m-%d %H:%M:%S}")
print(f"Local Now: {now:%c}")
print(f"AM/PM Now: {now:%I %p}")

print(f"{'Tip 5':=^51}")
n: float = 1234.5678
print(f"n = {n:.2f}")  # 1234.57
print(f"n = {n:.0f}")  # 1235
print(f"n = {n:,.3f}") # 1,234.568

print(f"{'Tip 6':=^51}")
a: int = 5
b: int = 10
my_var: str = "Hello world"
print(f"{a + b = }")          # a + b = 15
print(f"{bool(a) = }")        # bool(a) = True
print(f"my_var = {my_var}")   # my_var = Hello world
print(f"{my_var = }")         # my_var = 'Hello world'
print(f"my_var = {my_var!r}") # my_var = 'Hello world'
