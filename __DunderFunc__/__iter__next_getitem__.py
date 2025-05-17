"""
Python迭代器的基本方法: iter(), next()

迭代器：
    1. 迭代器是一个可以记住遍历的位置的对象. 它能在你调用next()方法时返回容器中的下一个值
    2. 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束. 迭代器只能往前不会后退.
    一个迭代器需要同时实现 __iter__() 和 __next__()
        __iter__(): 返回自身以获取该类的迭代器
        __next__(): 返回容器中的下一个元素, 当数据取完时, 要引发一个StopIteration异常

可迭代对象(Iterable)是能够一次性返回其成员的对象.
常见Iterable包括所有的序列类型(如list,str和tuple)以及一些非序列类型,
如dict和文件, 以及任何定义了__iter__()方法或__getitem__()的类的对象
(可以把自己的成员一个一个返回(或者说遍历自己的成员)的一类对象).

迭代器与列表的区别在于, 构建迭代器的时候, 不像列表把所有元素一次性加载到内存,
而是以一种延迟计算(lazy evaluation)方式返回元素

在迭代器中, __iter__ 和 __next__ 是必须的, 而 __init__ 不是

在 python 中, 实现了__iter__()方法的对象就是一个可迭代对象(Iterable),
实现了__iter()__ 和 __next()__方法的对象就是一个迭代器(Iterator)

iter(Iterable) return an Iterator
next(Iterator) return lazily produce next value

"""

print("====================== Fib =====================")
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
    break

###################################################
print("====================== Acu =====================")
# * 等差数列公式 an = a1 + (n-1) * d
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
print("====================== MyNumber =====================")
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

print("Next 1: ", next(my_iter))
print("Next 2: ", next(my_iter))
print("Next 3: ", next(my_iter))


print("====================== MyList =====================")
class MyList(list):
    def __init__(self, lst: list):
        self._lst = []
        for i in lst:
            self._lst.append(i + 2)

    def __iter__(self):
        # for each
        print('__iter__ called')
        return self._lst.__iter__()

    def __next__(self):
        print('__next__ called')
        return self._lst.__next__()

    def __getitem__(self, index):
        # [] operator
        print('__getitem__ called')
        return self._lst[index]

my_lst = MyList([1, 2, 3])
for i in my_lst:
    print(f"i = {i}")

print(f"{my_lst[0] = }")
print(f"{my_lst[1] = }")
print(f"{my_lst[2] = }")


class Person:
    def __getitem__(self, val):
        return f'__getitem__({val}) called.'

p = Person()
print(f"{p['some value'] = }")
print(f"{getattr(p, 'val', None) = }")
