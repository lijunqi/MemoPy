"""
sorted默认排序: 小->大
key: 是一个函数, 给list中每个元素对应一个函数值, 并按照这个函数值进行排序
"""

l = [1, 5, 4, 10, 9, 6]
output = sorted(l) # * sorted() return a new list, NOT inplace sorting
print("sorted: ", output) # [1, 4, 5, 6, 9, 10]

l = ['c', 'B', 'D', 'a']
print("sorted: ", sorted(l)) # ['B', 'D', 'a', 'c']

print("sorted upper: ", sorted(l, key=lambda s: s.upper())) # ['a', 'B', 'c', 'D']

# 2.
d = {'def': 300, 'abc': 200, 'ghi': 100}
# * sort by keys
print("sort by key d: ", sorted(d)) # ['abc', 'def', 'ghi']

# * sort by value
print("sort by value d: ", sorted(d, key=lambda e: d[e])) # ['ghi', 'abc', 'def']

# 3.
def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

l = [3+3j, 1-1j, 0, 3+0j]
print("sort by dist_sq", sorted(l, key=dist_sq)) # [0, (1-1j), (3+0j), (3+3j)]

# 4.
import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("random sort: ", sorted(l, key=lambda x: random.random()))
