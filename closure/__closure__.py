"""
判断一个函数是不是闭包, 可以查看它的closure属性.
如果该函数是闭包, 查看该属性将会返回一个cell对象组成的tuple.
如果我们分别对每个cell对象查看其cell_contents属性, 返回的内容就是闭包引用的自由变量的值
"""

def add(x,y):
    def f(z):
        return x+y+z
    return f

d = add(5,6)
d(9)
d(1)
for i in d.__closure__:
    print("d __closure__:", i.cell_contents)

def foo():
    print("this is foo.")

print("foo __closure__:", foo.__closure__)
