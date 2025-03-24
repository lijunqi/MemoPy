""" 
Reducing functions:
These are functions that recombine an iterable recursively, ending up with a single return value.
Also called accumulators, aggregators, or folding functions.

* These are functions that recombine an iterable recursively,
* ending up with a single return value.
* Also called accumulators, aggregators, or folding functions.

  def _reduce(fn, sequence, initial):
      res = initial
      for x in sequence:
          res = fn(res, x)
      return res
"""
from functools import reduce

l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y

_add = lambda x, y: x + y

print("reduce max lst:", reduce(_max, l)) # 10
print("reduce max set:", reduce(_max, {1, 3, 4, 5})) # 5

print("reduce add:", reduce(_add, l)) # 38


init = 111
print(reduce(lambda a, b: a+b, {1, 2, 3, 4}, init)) # 121
