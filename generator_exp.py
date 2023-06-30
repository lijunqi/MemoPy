import sys

'''
# memory
n = 10000000
a_list = [1 for i in range(n)]
a_gene = (1 for i in range(n))

print sys.getsizeof(a_list) # 40764032 bytes
print sys.getsizeof(a_gene) # 40 bytes
'''

rows =  [4, 2, 1, 5, 6]
seats = ['a', 's', 'd', 'f', 'q']

def foo():
    for row in rows:
        for s in seats:
            yield (row, "{}".format(s))

from pprint import pprint as pp
#pp(sorted(foo()))

gb = foo()
pp(next(gb)) # (4, 'a')
pp(next(gb)) # (4, 's')


def foo1(data):
    result = []
    for x in data:
        result.append(x * x)
    return result

def iter_foo(data):
    for x in data:
        yield x * x

def foo2(data):
    return list(iter_foo(data))

my_data = [1,2,3]
print foo1(my_data)
print foo2(my_data)
