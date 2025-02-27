"""
We have to explicitly tell Python we are modifying a nonlocal variable.

Whenever Python is told that a variable is nonlocal
  * it will look for it in the enclosing local scopes chain until it first encounters the specified vairable name
  * Beware: It will only look in local scopes, it will NOT look in the global scope
"""

def outer_func():
    x = 'hello'

    def inner_func():
        nonlocal x
        x = 'world'

    inner_func()
    print('x = ', x)

outer_func() # world


def outer():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()

    inner1()
    print(x) # python

outer()


def outer_2():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner(before), x = ', x) # python
        inner2()
        print('inner(after ), x = ', x) # monty

    inner1()
    print('outer_2, x = ', x) # hello

outer_2()
