from functools import wraps

def decorator_func_with_args(arg1, arg2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Before orginal function with decorator args:", arg1, arg2)
            print('function name: ', func.__name__)
            result = func(*args, **kwargs)
            print("Ran after the orginal function")
            return result
        return wrapper
    return decorator
 
 
@decorator_func_with_args("test1", "test2")
def hello(name):
    """A function which prints a greeting to the name provided.
    """
    print('Hello ', name)
    return 25
 
 
print("Starting script...")
x = hello('Jacky')
print("The value of x is:", x)
print("The wrapped functions docstring is:", hello.__doc__)
print("The wrapped functions name is:", hello.__name__)
