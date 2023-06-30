""" mypy . """
import typing as t

T = t.TypeVar('T', int, str)

def foo(x: T) -> None:
    print('x = ', x)

foo(1)
foo("123")
foo([1,2,3]) # error: Value of type variable "T" of "foo" cannot be "List[int]"  [type-var]

num1: T = 1
num2: T = "456"
num3: T = [4,5,6]
print(t.TYPE_CHECKING)