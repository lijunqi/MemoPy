""" 
When a type hint contains names that have not been defined yet,
that definition may be expressed as a string literal, to be resolved later.

If no double quotes. NameError
"""

def foo(a: int, b: "BaseA") -> None:
    print("This is a: ", a)
    print("This is b: ", b)

class BaseA():
    def __init__(self) -> None:
        pass

foo(123, BaseA())
