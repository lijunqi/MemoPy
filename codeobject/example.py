def f():
    pass

print(f.__code__)

code = f.__code__
print(code.co_code)

print('============')
print(code.co_name)
print(code.co_filename)
print(code.co_lnotab)
