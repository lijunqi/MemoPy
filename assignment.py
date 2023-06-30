# coding: utf-8

'''
python中, 万物皆对象. python中不存在所谓的传值调用, 一切传递的都是对象的引用, 也可以认为是传址
python中, 对象分为可变(mutable)和不可变(immutable)两种类型
元组(tuple), 数值型(number), 字符串(string)均为不可变对象, 而字典型(dictionary)和列表型(list)的对象是可变对象
'''
a = 1 # a point to object '1'
a = 2 # 将a与内存中值为2的内存绑定在一起, 而不是修改原来a绑定的内存中的值, 这时, 内存中值为1的内存地址引用计数-1, 当引用计数为0时, 内存地址被回收
b = a # b point to a
b = 3 # b point to a new object '3', a is still 2

a = [1,2,3]
b = a # b is [1,2,3]
b.remove(1) # a and b both are [2,3]
b = [4,5,6] # b point to new object [4,5,6], a is [2,3]

b = 256
id(b) == id(256) # True
c = 257
id(c) == id(257) # False


'''
1. 切片操作和工厂方法list方法都是浅拷贝，只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。
2. 利用copy中的deepcopy方法是深拷贝，外围和内部元素都进行了拷贝对象本身，而不是引用。
3. 对于数字，字符串和其他原子类型对象等，没有被拷贝的说法，即便是用深拷贝，查看id的话也是一样的，如果对其重新赋值，也只是新创建一个对象，替换掉旧的而已。
'''
Tom = ['Tom', ['age', 10]]
Jack = Tom[:]
June = list(Tom)

'''
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
'''

Jack[1][1] = 20
print Tom, Jack, June
