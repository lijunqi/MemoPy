# coding: utf-8

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
