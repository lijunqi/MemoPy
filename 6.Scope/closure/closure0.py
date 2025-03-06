"""
Python Cells and Multi-Scoped Variables
"""

# * Here the value of x is shared between 2 scopes: outer_func and inner_func(closure)
# * The label x is in 2 different scopes, but always reference the same "value"
# * Python does this by creating a cell as an intermediary object.
# * Cell gets used when you have a closure.
def outer_func():
    x = 'python'
    def inner_func():
        print(x)
    return inner_func


"""
The closure is created when the function is created, that's when Python decides it's a closure.
It's going to use that cell and it's going to do the double hop eventually.
But it doesn't evaluate the value of the free variable until you call the function in that closure.

A function only becomes a closure if it has a free variable.
Free variable is those who not parameter of function or not define in function.
"""
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

f1, f2 = outer()
print("f1() = ", f1()) # output: 1
print("f2() = ", f2()) # output: 2


###### Shared Extended Scopes ######

# "n" and "inner" are closure
def adder(n):
    def inner(x):
        return x + n
    return inner

# 3 different closures - no shared scopes
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print("add_1(10) = ", add_1(10)) # 11
print("add_2(10) = ", add_2(10)) # 12
print("add_3(10) = ", add_3(10)) # 13


# * For loop creates 3 closures, all n in 3 closures are point to the same cell. They share the same cell.
# * n is evaluated when the closure(function) is called.
# lambda create function.
# n = 1: the free variable in the lambda is n, and it is bound to the n we created in the loop
# n = 2: the free variable in the lambda is n, and it is bound to the (same) n we created in the loop
# n = 3: the free variable in the lambda is n, and it is bound to the (same) n we created in the loop
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

print("adders[0](10) = ", adders[0](10)) # 13
print("adders[1](10) = ", adders[1](10)) # 13
print("adders[2](10) = ", adders[2](10)) # 13

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()
print(adders[0].__closure__, adders[1].__closure__, adders[2].__closure__) # They point to the same cell
print("adders[0](10) = ", adders[0](10)) # 13

# *
def create_adders2():
    adders = []
    for N in range(1, 4):
        # * Defaults get evaluated at creation time
        # * So when this lambda is created, the default value of N, whatever N is, is going to be used.
        # * So when N is 1, Y will have a default value of 1,
        # * it will not have a default value pointing to the cell.
        # * In this case, we're not event creating closures. We're just creating functions.
        adders.append(lambda x, Y=N: x + Y)
    return adders

adders = create_adders2()
print("[Good] adders[0](10) = ", adders[0](10)) # 11
print("[Good] adders[1](10) = ", adders[1](10)) # 12
print("[Good] adders[2](10) = ", adders[2](10)) # 13


###### Nested Closures ######
def incrementer(n):
    # inner + n is a closure
    def inner(start):
        current = start
        # inc + current + n is a closure
        def inc():
            nonlocal current
            current += n
            return current

        return inc
    return inner

fn = incrementer(2) # fn.__code__.co_freevars -> 'n'  n=2
inc_2 = fn(100) # inc_2.__code__.co_freevars -> 'current', 'n'

inc_2() # 102 (current = 102, n = 2)
inc_2() # 104 (current = 104, n = 2)
