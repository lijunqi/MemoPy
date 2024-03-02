from inspect import (
    isfunction,
    ismethod,
    isroutine,
    getsource,
    getcomments,
    getmodule,
)
import main

# TODO: todo my func
def my_func():
    pass

print("my_func is function: ", isfunction(my_func))
print("my_func is method: ", ismethod(my_func))
print("my_func is routine: ", isroutine(my_func))

"""
Classes and objects have attributes - an object that is bound to the class or the object
An attribute that is callable, is called a method
"""
class MyClass:
    def func(self):
        pass

my_obj = MyClass()
print("my_obj.func is function: ", isfunction(my_obj.func))
print("my_obj.func is method  : ", ismethod(my_obj.func))
print("my_obj.func is routine : ", isroutine(my_obj.func))

print("getsource(my_func)  : ", getsource(my_func))
print("getsource(main)     : ", getsource(main))
print("getcomments(my_func): ", getcomments(my_func))
print("getcomments(main)   : ", getcomments(main))

print("getmodule(my_func): ", getmodule(my_func))
print("getmodule(main)   : ", getmodule(main))
print("getmodule(print)  : ", getmodule(print))
