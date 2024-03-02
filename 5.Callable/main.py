
print("print is callable: ", callable(print))       # True
print("'abc'.upper is callable: ", callable('abc'.upper)) # True
print("str.upper is callable: ", callable(str.upper))   # True
print("callable is callable: ", callable(callable))    # True

print("10 is callable: ", callable(10))    # False
