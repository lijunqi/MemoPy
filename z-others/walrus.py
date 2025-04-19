
def foo1():
    return [1,2,3]

def foo2():
    return []

def foo3():
    return None

if x := foo1():
    print("x = ", x)

if y := foo2():
    print("y = ", y)
else:
    print("y is empty")

if z := foo3():
    print("z = ", z)
else:
    print("z is empty")

