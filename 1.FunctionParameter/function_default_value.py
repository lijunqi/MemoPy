"""
* In general, always beware of using a mutable object (or a callable)
* for an argument default
"""

# Module Code
def func(a=10):   # the function object is created, and func references it
    print(a)      # the integer object 10 is evaluated/created
                  # and is assigned as the default for a

func()            # the function is executed
                  # by the time this happens, the default value for a has already been
                  #!evaluated and assigned - it is NOT re-evaluated when the function is called

import time
from datetime import datetime

def log(msg, *, dt=datetime.utcnow()):
    print(f"{msg}: {dt}")

log("message 1")
time.sleep(1)
log("message 2") # ! xxx dt of message 1 and 2 are equal.
                 # Because dt is evaluated when function log is defined,
                 # NOT when log is called

def log2(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f"{msg}: {dt}")


# 2.
def add_item(name, quantity, unit, grocery_list=[]):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list

store1 = add_item('banana', 2, 'unit')
add_item('milk', 1, 'liter', store1)
print("store1: ", store1)

store2 = add_item('apple', 3, 'unit')
print("After add apple:")
print("store2: ", store2)
print("store1: ", store1)
print("store1 is store2: ", store1 is store2) # True
