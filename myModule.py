print("This is myModule.")

a = 123

def foo(x):
    return x + x

def double_it(x: int):
    return 2 * x

print("Quit myModule.")

def t():
    try:
        return "try"
    finally:
        return "finally"

print(t())
