"""
! Beware:
! "nonlocal" will only look in local scopes,
! it will NOT look in the global scope
"""

x = 123

def outer():
    global x
    x = 'monty'

    def inner():
        nonlocal x # No binding for nonlocal "x" found
        x = 'hello'

    inner()
    print(x)

outer()
