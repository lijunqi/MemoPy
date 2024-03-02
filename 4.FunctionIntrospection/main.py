""" This is main file """

def my_func1(a, b=2, c=3, *, kw1, kw2=2):
    pass

print("my_func1.__name__: ", my_func1.__name__) # my_func1
print("my_func1.__defaults__: ", my_func1.__defaults__) # (2, 3)
print("my_func1.__kwdefaults__: ", my_func1.__kwdefaults__) # {'kw2': 2}

def my_func2(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

print("my_func2.__code__: ", my_func2.__code__)

# * parameter names first, followed by local variable names
# ('a', 'b', 'args', 'kwargs', 'i')
print("my_func2.__code__.co_varnames: ", my_func2.__code__.co_varnames)

# * number of parameters (does NOT count *args and **kwargs)
print("my_func2.__code__.co_argcount: ", my_func2.__code__.co_argcount) # 2
