"""
! Positional arguments
    ! may have default values
    *args: collects, and Exhausts Remaining positional arguments
    *: indicates no more positional arguments(effectively exhausts)

! Keyword arguments
    ! may have default values
    ! after positional arguments have been exhausted
    **kwargs: collects any remaining keyword arguments

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
    pass


func(1, 2, a=10, b=20)
# args = (1, 2)
# kwargs = {'a': 10, 'b': 20}


func()
# args = ()
# kwargs = {}


print("========= Call func1(1, 2, x=100, y=200, d=20) =========")
def func1(a, b, *, d, **kwargs):
    print('a =', a)
    print('b =', b)
    print('d =', d)
    print('kwargs =', kwargs)

func1(1, 2, x=100, y=200, d=20)
