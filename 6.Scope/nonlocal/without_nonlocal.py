
def outer_func():
    x = 'hello' # This is local variable x in outer_func

    def inner_func():
        x = 'world' # This is local variable x in inner_func

    inner_func()
    print('x = ', x)

outer_func() # hello
