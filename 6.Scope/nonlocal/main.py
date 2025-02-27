"""
We have to explicitly tell Python we are modifying a nonlocal variable.
"""

def outer_func():
    x = 'hello'

    def inner_func():
        nonlocal x
        x = 'world'

    inner_func()
    print('x = ', x)

outer_func() # world
