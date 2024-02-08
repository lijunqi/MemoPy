"""
python中, 万物皆对象.
python中, 一切传递的都是对象的引用, 也可以认为是传址
python中, 对象分为:
    可变(mutable): dict, list
    不可变(immutable): tuple, string, number
"""

a = 1 # a point to object '1'
a = 2 # 将a与内存中值为2的内存绑定在一起, 而不是修改原来a绑定的内存中的值,
      # 这时, 内存中值为1的内存地址引用计数-1, 当引用计数为0时, 内存地址被回收
b = a # b point to a
b = 3 # b point to a new object '3', a is still 2

a = [1,2,3]
b = a # b is [1,2,3]
b.remove(1) # a and b both are [2,3]
b = [4,5,6] # b point to new object [4,5,6], a is [2,3]

b = 256
print(id(b) == id(256)) # True
c = 257
print(id(c) == id(257)) # False


"""
1. 切片操作和工厂方法list方法都是浅拷贝, 只是拷贝了最外围的对象本身, 内部的元素都只是拷贝了一个引用而已。
2. 利用copy中的deepcopy方法是深拷贝, 外围和内部元素都进行了拷贝对象本身, 而不是引用。
3. 对于数字, 字符串和其他原子类型对象等, 没有被拷贝的说法,
   即便是用深拷贝, 查看id的话也是一样的, 如果对其重新赋值, 也只是新创建一个对象, 替换掉旧的而已.
"""
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
print(Tom, Jack, June)


# * Unpacking
print("========= Unpacking =========")
lst = [1,2,3,4,5,6]
a, *b = lst     # 等同于: a, b = lst[0], lst[1:]
print(f"a = {a}, b = {b}")

# The * operator(the rest) can only be used ONCE in the LHS an unpacking assignment
a, b, *c, d = lst
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

a, b, *c, d = 'python'
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

l1 = [1,2,3]
l2 = [4,5,6]
print("[*l1, *l2] =", [*l1, *l2]) # [1, 2, 3, 4, 5, 6]
print("[l1, l2] =", [l1, l2])     # [[1, 2, 3], [4, 5, 6]]

l2 = 'XYZ'
print("[*l1, *l2] =", [*l1, *l2]) # [1, 2, 3, 'X', 'Y', 'Z']

# When working with dictionaries, * operator iterated the keys
d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7} # key 'h' in both d2 and d3
print("[*d1, *d2, *d3] =", [*d1, *d2, *d3]) # ['p', 'y', 't', 'h', 'h', 'o', 'n']
print("{*d1, *d2, *d3} =", {*d1, *d2, *d3}) # {'n', 'y', 'h', 'o', 't', 'p'}    Order is NOT guaranteed

# Using **, ** operator can NOT be used in the LHS of an assignment
d = {**d1, **d2, **d3}
print("{**d1, **d2, **d3} =", d) # {'p': 1, 'y': 2, 't': 3, 'h': 5, 'o': 6, 'n': 7}
                                 # ! 'h' in d3 overwrite the first value of 'h' in d2

# Nested Unpacking
a, b, (c, d) = [1, 2, [3, 4]]
print(f"a = {a}, b = {b}, c = {c}, d = {d}") # a = 1, b = 2, c = 3, d = 4

a, *b, (c, d, e) = [1, 2, 3, 'XYZ']
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}") # a = 1, b = [2, 3], c = X, d = Y, e = Z
