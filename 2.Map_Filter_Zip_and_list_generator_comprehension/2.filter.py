"""
filter(func, iterable)
    1. func: some function that takes a single argument
    2. iterable: a single iterable

filter(func, iterable) will then return an iterator that
contains all the elements of the iterable for which the function called on it is Truthy.

* It allow us to specify a function that determines wheter we retain or throw out
* the elements of that iterable.
func takes a single argument, retain if it return true, throw if it return false.

* If the function is None, it returns the elements of iterable that are Truthy.
"""

l = [0, 1, 2, 3, 4]
print(list(filter(None, l))) # [1, 2, 3, 4]

def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, l))) # [0, 2, 4]
print(list(filter(lambda n: n % 2 == 0, l))) # [0, 2, 4]


l = range(10)
res = list(filter(lambda y: y < 25, map(lambda x: x**2, l))) # == [x**2 for x in range(10) if x**2 < 25]
print(res) # [0, 1, 4, 9, 16]
