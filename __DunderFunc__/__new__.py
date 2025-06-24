""" Define a singleton class
"""
class Singleton(object):
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            #cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(("s1 is s2: %s") % (s1 is s2))


class A(object):
    def __new__(cls, *args, **kwargs):
        print("cls is", cls.__name__)
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
        print('cls: ', cls.__name__)
        print('func: ', func)
        print('params: ', params)

    def __init__(self) -> None:
        print('Enter B init')
        print('Leave B init')

def foo():
    print('foo')

b = B(foo, 1, 2, 3)


# * Order of __new__ and __init__
print("========= Metaclass =========")
class Parent(type):
    def __new__(cls, *args, **kwargs):
        print("This is Parent __new__")
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(cls, name, bases, dct):
        print("This is Parent __init__")
        super().__init__(name, bases, dct)

class Child(metaclass=Parent):
    def __new__(cls):
        print("This is Child __new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("This is Child __init__")
        return super().__init__()

c1 = Child()


print("========= Normal class =========")
class Parent2(object):
    def __new__(cls, *args, **kwargs):
        print("This is Parent2 __new__")
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self):
        print("This is Parent2 __init__")
        super().__init__()

class Child2(Parent2):
    def __new__(cls):
        print("This is Child2 __new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("This is Child2 __init__")
        return super().__init__()

c2 = Child2()
