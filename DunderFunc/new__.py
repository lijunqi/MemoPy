""" Define a singleton class
"""
class Singleton(object):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(("s1 is s2: %s") % (s1 is s2))


class A(object):
    def __new__(cls, *args, **kwargs):
        print("Enter A's __new__()")
        print("Leave A's __new__()")
        # * Must have a return value
        return object.__new__(cls) # return self to __init__ func
    
    def __init__(self) -> None:
        print("Enter A's __init__()")
        print("Leave A's __init__()")
    
    def __call__(self, *args, **kwds):
        print('Call A')

a = A()
print('Complete init a')
a()

class B():
    def __new__(cls, *args, **kwargs):
        func, *params = args
        print('cls: ', cls)
        print('func: ', func)
        print('params: ', params)

    def __init__(self) -> None:
        print('Enter B init')
        print('Leave B init')

def foo():
    print('foo')

b = B(foo, 1, 2, 3)
