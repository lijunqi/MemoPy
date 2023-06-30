# coding: utf-8

'''

'''

x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)
# inner: 2
# outer: 1
# global: 0

print("=========================")

x = 12

def f1():
    x = 3
    print(x)

def f2():
   #err x += 1
    print(x)

f1()
f2()

print("=========================")

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(111111)



print(True == False == False) # equals (True == False and False == False)

# nonlocal is supported in Python3.0 and later
# x = 0
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print("inner:", x)
# 
#     inner()
#     print("outer:", x)
# 
# outer()
# print("global:", x)
# inner: 2
# outer: 2
# global: 0
