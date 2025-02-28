
x = 100
def outer():
    x = 'python'

    def inner1():
        nonlocal x
        x = 'monty'
        def inner2():
            global x
            x = 'hello'
        print('inner(before)', x) # output: monty
        inner2()
        print('inner(after )', x) # output: monty

    inner1()
    print('outer', x) # output: monty

outer()

print(x) # output: hello
