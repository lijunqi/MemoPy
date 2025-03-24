"""
zip(*iterables): takes in multiple iterables and return 1 iterable.

* The iterator stops as soon as one of the iterables has been exhausted.
* It's not a higher order function.
"""

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
print(list(zip(l1, l2))) # [(1, 10), (2, 20), (3, 30), (4, 40)]

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
print(list(zip(l1, l2))) # [(1, 10), (2, 20), (3, 30)]

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
l3 = 'python'
print(list(zip(l1, l2, l3))) # [(1, 10, 'p'), (2, 20, 'y'), (3, 30, 't')]

l1 = range(100)
l2 = 'abcd'
print(list(zip(l1, l2))) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]


l1 = [1, 2, 3]
l2 = [10, 20, 30]
res = [x+y for x, y in zip(l1, l2)] # == list(map(lambda x, y: x + y, l1, l2))
print(res) # [11, 22, 33]
