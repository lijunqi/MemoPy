"""
These are functions that recombine an iterable recursively, ending up with a single return value.
Also called accumulators, aggregators, or folding functions.
"""
from functools import reduce

l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y

_add = lambda x, y: x + y

print("reduce max lst:", reduce(_max, l)) # 10
print("reduce max set:", reduce(_max, {1, 3, 4, 5})) # 5

print("reduce add:", reduce(_add, l)) # 38
