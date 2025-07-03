""" User-defined generic types """
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    """
    Generic[T] as a base class defines that the class LoggedVar takes a single type parameter T.
    This also makes T valid as a type within the class body.
    """
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)


###################################################################

# Generics can be parameterized by using a factory available in typing called TypeVar.

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]

l = [1, 2, 3]
print(first(l))

t = tuple(('abc', 1, 2))
print(first(t))
