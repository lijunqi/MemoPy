"""
Python迭代器的基本方法: iter(), next()
迭代器：
    1. 迭代器是一个可以记住遍历的位置的对象。
    2. 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

Iterable是能够一次性返回其成员的对象.
常见Iterable包括所有的序列类型(如list,str和tuple)以及一些非序列类型,
如dict和文件, 以及任何定义了__iter__()方法或__getitem__()的类的对象
(可以把自己的成员一个一个返回(或者说遍历自己的成员)的一类对象).
"""

class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        print('__iter__ called')
        self.a = 0
        self.b = 1
        print('__iter__ done')
        return self

    def __next__(self):
        print('__next__ called')
        fib = self.a
        if fib > self.max:
            print("xxx Stop Iteration!")
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        print('__next__ return ', fib)
        return fib

cnt = 0
for val in Fib(5):
    print(f"    Fib({cnt}) = {val}")
    cnt += 1

###################################################
print("===========================================")
# 等差数列公式 an = a1 + (n-1) * d
class Acu():
    def __init__(self, a1, d, n):
        self.a1 = a1
        self.d = d
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        an = self.a1
        if an > self.n:
            raise StopIteration
        else:
            self.a1 += self.d 
            return an

#for i in Acu(1, 2, 15):
#    print(i)

###################################################
print("===========================================")
class MyNumber:
    def __iter__(self):
        print('__iter__ called')
        self.a = 1
        print('__iter__ done')
        return self

    def __next__(self):
        print('__next__ called')
        x = self.a
        self.a += 1
        print('__next__ return ', x)
        return x

my_class = MyNumber()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
