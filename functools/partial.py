"""

Key Features and Benefits:

1. Argument Fixing:
    It allows you to pre-populate arguments, reducing the number of arguments needed for subsequent calls.
2. Specialized Functions:
    Creates specialized versions of general-purpose functions, making code more readable and focused.
3. Cleaner Code:
    Can simplify code by avoiding repetitive argument passing
    or complex lambda expressions in certain scenarios.
4. Constructor Specialization:
    Can be used with class constructors to create specialized object instantiation with predefined parameters.
"""
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print("double(3) = ", double(3))


def foo(a, b, c, *args, **kwargs):
    print(" foo ".center(20, "="))
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("args = ", args)
    print("kwargs = ", kwargs)

f1 = partial(foo, a=123)
f1(b="b", c="c")

f2 = partial(foo, a=123, stage="f2 stage", timeout=99)
f2(b="bb", c="cc")
