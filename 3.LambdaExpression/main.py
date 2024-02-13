"""
lambda [parameter list]: expression

the expression returns a function object which not named.
(anonymous function)

Limitations:
* The "body" of a lambda is limited to a single expression, so...
    * 1. No assignments
    * 2. No annotations

Example:
    lambda x: x**2
    lambda x, y=10: x + y   # default value
    lambda : 'hello'
    lambda s: s[::-1].upper()
    lambda x, *args, y, **kwargs: (x, args, y, kwargs)
"""

my_func = lambda x: x**2
print("my_func(4) =", my_func(4))
