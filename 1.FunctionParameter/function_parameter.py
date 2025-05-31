"""
! Positional arguments (may have default values)
    *args: collects, and Exhausts Remaining positional arguments
    *: indicates no more positional arguments(effectively exhausts):
       All following arguments are keyword-only arguments.
       That is, they can only be provided using their name, not as positional argument.

! Keyword arguments (may have default values)
    ! after positional arguments have been exhausted
    **kwargs: collects any REMAINING keyword arguments

        a, b, c=10   *args/*   kw1, kw2=100   **kwargs
        ----------
positional parameters
a, b are mandatory


def func(a, b=10)

def func(a, b, *args)

def func(a, b, *args, kw1, kw2=100)

def func(a, b=10, *, kw1, kw2=100)

def func(a, b, *args, kw1, kw2=100, **kwargs)

def func(a, b=10, *, kw1, kw2=100, **kwargs)

def func(*args)

def func(**kwargs)

def func(*args, **kwargs)

"""

def func(*args, **kwargs):
    print('args =', args)
    print('kwargs =', kwargs)


func(1, 2, a=10, b=20)
# Output:
# args = (1, 2)
# kwargs = {'a': 10, 'b': 20}


func()
# Output:
# args = ()
# kwargs = {}

func(1, 2, 3, 4, 5)
# Output:
# args = (1, 2, 3, 4, 5)


print("========= Call func1(1, 2, x=100, y=200, d=20) =========")
def func1(a, b, *, d, **kwargs):
    print('a =', a)
    print('b =', b)
    print('d =', d)
    # ! x, y in kwargs: kwargs = {'x': 100, 'y': 200}
    print('kwargs =', kwargs)

func1(1, 2, x=100, y=200, d=20)


print("========= Call func2(1, 2, 3, 4, x=100, y=200, d=20) =========")
def other_func(a, b):
    print('other func, a =', a)
    print('other func, b =', b)
    print('type b =', type(b))

def func2(*args, **kwargs):
    print('args =', args)
    print('kwargs =', kwargs)
    print('x = ', kwargs.get('x'))
    print('y = ', kwargs.get('y'))
    other_func(1, args)
    other_func(2, kwargs)

func2(1, 2, 3, 4, x=100, y=200, z=300)


print("========= Call func3(123, 456, 789, x=1, y=2, d=3) =========")
def func3(a, b, c, **kwargs):
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('kwargs =', kwargs)
    print('kwargs["x"] =', kwargs['x'])
    print('kwargs["y"] =', kwargs.get('y', -1))
    print('kwargs["z"] =', kwargs.get('z', -1))

func3(123, 456, 789, x=1, y=2, d=3)
