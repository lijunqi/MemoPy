""" nonlocal """

def outer():
    x = 'hello'

    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner(before)', x) #  output:python
        inner2()
        print('inner(after )', x) # output: monty

    inner1()
    print('outer', x) # output: monty

outer()
