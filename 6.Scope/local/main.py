"""
Assignment -> Python interprets assignment as a local variable (at compile-time)

a = 0
def my_func():
    print(a) # a is unbound
    a = 123  # runtime error
"""

a = 0
def my_func():
    a = 100 # Python interprets as a local variable at compile-time
    print("a = ", a)

my_func() # 100
print(a) # 0
