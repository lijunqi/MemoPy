"""
判断一个函数是不是闭包, 可以查看它的closure属性.
如果该函数是闭包, 查看该属性将会返回一个cell对象组成的tuple.
如果我们分别对每个cell对象查看其cell_contents属性, 返回的内容就是闭包引用的自由变量的值

The closure is created when the function is created, that's when Python decides it's a closure.
It's going to use that cell and it's going to do the double hop eventually.
But it doesn't evaluate the value of the free variable until you call the function in that closure.
"""

def add(x,y):
    def f(z):
        return x+y+z
    return f

fn = add(5,6)
fn(9)
fn(1)
for i in fn.__closure__:
    print("fn __closure__, cell_contents:", i.cell_contents)

def foo():
    print("this is foo.")

print("foo __closure__:", foo.__closure__)

print("fn free vars: ", fn.__code__.co_freevars)
