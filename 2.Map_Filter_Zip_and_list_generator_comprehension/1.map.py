"""
map(func, *iterables)
    1. func: some function that takes as many arguments as there are iterable objects passed to "iterables"
    2. *iterables: a variable number of iterable objects

map(func, *iterables) will then return an iterator that
calculates the function applied to each element of the iterables.

* The iterator stops as soon as one of the iterables has been exhausted
"""

l = [2, 3, 4]
def sq(x):
    return x**2

print(list(map(sq, l))) # [4, 9, 16]

l1 = [1, 2, 3]
l2 = [10, 20, 30]
def add(x, y):
    return x + y

print(list(map(add, l1, l2))) # [11, 22, 33]
print(list(map(lambda x, y: x + y, l1, l2))) # [11, 22, 33]
