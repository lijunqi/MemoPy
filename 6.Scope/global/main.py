"""
We saw how to use the global keyword in order to
modify a global variable within a nested scope.
"""

a = 10
def outer_func1():
    global a
    a = 1000

outer_func1()
print(a) # 1000

def outer_func2():
    def inner_func():
        global a
        a = 'hello'
    inner_func()

outer_func2()
print(a) # hello
