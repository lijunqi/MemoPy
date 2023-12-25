"""
在一些语言中, 在函数中可以(嵌套)定义另一个函数时,
如果内层函数引用了外层函数的变量, 则可能产生闭包.
闭包可以用来在一个函数与一组"私有"变量之间创建关联关系.
在给定函数被多次调用的过程中, 这些私有变量能够保持其持久性

1. 闭包是将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁
2. 将外层函数的变量持久地保存在内存中

总结:
    局部变量无法共享和长久的保存, 而全局变量可能造成变量污染, 闭包既可以长久的保存变量又不会造成全局污染.
    闭包使得函数内局部变量的值始终保持在内存中, 不会在外层函数调用后被自动清除.
    当外层函数返回了内层函数后, 外层函数的局部变量还被内层函数引用.
    带参数的装饰器, 那么一般都会生成闭包.
    闭包在爬虫以及web应用中都有很广泛的应用.

# https://zhuanlan.zhihu.com/p/453787908
"""

def study_time():           # 外层函数
    time = 0                # 外层函数变量
    def insert_time(min):   # 内部函数
        nonlocal time
        time = time + min
        return time
    return insert_time


f = study_time()

time_in_studytime = f(2)
print("time in study_time():", time_in_studytime)

time_in_studytime = f(10)
print("time in study_time():", time_in_studytime)


# * 闭包无法改变外层函数局部变量指向的内存地址
def outer_fun1():
    x = 123456
    def inner_fun():
        x = 456789
        print('    inner x:',x, 'at', id(x))

    print('outer1 x before call inner:', x, 'at', id(x))
    inner_fun()
    print('outer1 x after  call inner:', x, 'at', id(x))
    
outer_fun1()

# * 如果要让内层函数不仅可以访问, 还要可以修改外层函数的变量,
# * 那么需要用到nonlocal声明, 使得内层函数不要在自己的命名空间创建新的x, 而是操作外层函数命名空间的x.
def outer_fun2():
    x = 123456
    def inner_fun():
        nonlocal x  #! 注意这里
        x = 456789
        print('    inner x:',x, 'at', id(x))

    print('outer2 x before call inner:', x, 'at', id(x))
    inner_fun()
    print('outer2 x after  call inner:', x, 'at', id(x))
    
outer_fun2()
