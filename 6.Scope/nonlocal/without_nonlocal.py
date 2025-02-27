
def outer_func():
    x = 'hello'

    def inner_func():
        x = 'world'

    inner_func()
    print('x = ', x)

outer_func() # hello
