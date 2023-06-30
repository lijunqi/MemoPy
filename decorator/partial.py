from functools import partial

def foo(a, b):
    return 2*a + b

foo2 = partial(foo, 2)

print('foo(1, 2) = ', foo(1, 2)) # ans = 4
print('foo2(3) = ', foo2(3)) # ans = 7
