from typing import Any, TypeVar, Final

# ! type of number is Any, not very meaningful
def identity(arg: Any) -> Any:
    return arg
number = identity(42)
#print(number + "!")


# ! This doesn't scale well.
# ! You need to replicate many functions for different types
def identity_int(arg: int) -> int:
    return arg
number = identity_int("zzz")
print(number + "!")


# * Pylance will tell you type of number1, number2 and number3
T = TypeVar("T")
def identity2(arg: T) -> T:
    return arg
number1 = identity2(42)
number2 = identity2("asdf")
number3 = identity2([1,2,3])

# * Putting constraints on a type variable
AnyString = TypeVar("AnyString", str, bytes)
def triple(string: AnyString) -> AnyString:
    return string * 3

unicode_scream = triple("A") + "!"
bytes_scream = triple(b"A") + b"!"
print(unicode_scream, bytes_scream)


# * Cannot be re-assigned or overridden in a subclass
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker
