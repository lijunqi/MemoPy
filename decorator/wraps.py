from functools import wraps
 
def a_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        print('In wrapper... Function name: ', func.__name__)
        # Extend some capabilities of func
        func(*args, **kwargs)
    return wrapper
 
@a_decorator
def first_function(a):
    """This is docstring for first function"""
    print("This is first function")
    print('a = ', a)

print('=== Call func ===')
first_function(123)

print('func name: ', first_function.__name__) # first_function
print('func doc : ', first_function.__doc__)
