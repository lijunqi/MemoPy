
def foo1():
    return [1,2,3]

def foo2():
    return []

if x := foo1():
    print("x = ", x)

if y := foo2():
    print("y = ", y)
else:
    print("y is empty")
