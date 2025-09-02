"""
python中, 万物皆对象.
python中, 一切传递的都是对象的引用, 也可以认为是传址
python中, 对象分为:
    可变(mutable): dict, list
    不可变(immutable): tuple, string, number
"""

a = 1  # a point to object '1'
a = 2  # 将a与内存中值为2的内存绑定在一起, 而不是修改原来a绑定的内存中的值,
# 这时, 内存中值为1的内存地址引用计数-1, 当引用计数为0时, 内存地址被回收
b = a  # b point to a
b = 3  # b point to a new object '3', a is still 2

a = [1, 2, 3]
b = a  # b is [1,2,3]
b.remove(1)  # a and b both are [2,3]
b = [4, 5, 6]  # b point to new object [4,5,6], a is [2,3]

b = 256
print(id(b) == id(256))  # True
c = 257
print(id(c) == id(257))  # False


###############################################################################


# * a and b are Parameters of my_func. a and b are local to my_func
def my_func(a, b):
    a = 123
    b = 456


# * x and y are Arguments of my_func
# * x and y are passed by reference, i.e. pass the memory address
x = 10
y = "a"
my_func(x, y)
print("x = ", x)
print("y = ", y)


# ! Positional Arguments
# * If a positional parameter is defined with a default value,
# * EVERY positional parameter after it MUST also be given a default value
print("====== Positional Arguments ======")


def func1(*args, d):
    print(f"args = {args}, d = {d}")


func1(1, 2, 3, d=100)


# In fact we can force no positional arguments at all:
# "*" indicates the "end" of positional arguments
def func2(*, d):
    print(f"d = {d}")


func2(d=123)

# ! Keyword Arguments
# * All arguments after the first named(keyword) argument, MUST be named too.
# * Default arguments may still be omitted.
print("====== Keyword Arguments ======")


"""
1. 切片操作和工厂方法list方法都是浅拷贝, 只是拷贝了最外围的对象本身, 内部的元素都只是拷贝了一个引用而已。
2. 利用copy中的deepcopy方法是深拷贝, 外围和内部元素都进行了拷贝对象本身, 而不是引用。
3. 对于数字, 字符串和其他原子类型对象等, 没有被拷贝的说法,
   即便是用深拷贝, 查看id的话也是一样的, 如果对其重新赋值, 也只是新创建一个对象, 替换掉旧的而已.
"""
Tom = ["Tom", ["age", 10]]
Jack = Tom[:]
June = list(Tom)

"""
!!! copy !!!
>>> for x in Tom:
... print id(x)
... 
140704715293600 --> 'Tom'
140704715147816 --> ['age', 20]
>>> for x in Jack: 
... print id(x)
... 
140704715286256 --> 'Jack'
140704715147816 --> ['age', 20]
>>> for x in June:
... print id(x)
... 
140704715286352 -->'June'
140704715147816 -->['age', 20]


!!! Deep copy !!!
>>> import copy
>>> Tom = ['Tom', ['age', 10]]
>>> Jack = copy.deepcopy(Tom)
>>> June = copy.deepcopy(Tom)
"""

Jack[1][1] = 20
print(Tom, Jack, June)
