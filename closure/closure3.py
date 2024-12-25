""" 返回闭包时，返回函数不要引用任何循环变量，或者后续会发生变化的变量 """

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print("f1() =", f1()) # 9
print("f2() =", f2()) # 9
print("f3() =", f3()) # 9

print("=====================")
"""
如果一定要引用循环变量怎么办?
方法是再创建一个函数, 用该函数的参数绑定循环变量当前的值,
无论该循环变量后续如何更改, 已绑定到函数参数的值不变
"""
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  #! f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = count2()
print("f4() =", f4()) # 1
print("f5() =", f5()) # 4
print("f6() =", f6()) # 9
