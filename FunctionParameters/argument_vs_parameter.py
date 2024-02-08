
# * a and b are Parameters of my_func. a and b are local to my_func
def my_func(a, b):
    a = 123
    b = 456

# * x and y are Arguments of my_func
# * x and y are passed by reference, i.e. pass the memory address
x = 10
y = 'a'
my_func(x, y)
print("x = ", x)
print("y = ", y)


# ! Positional Arguments
# * If a positional parameter is defined with a default value,
# * EVERY positional parameter after it MUST also be given a default value

# ! Keyword Arguments
# * All arguments after the first named(keyword) argument, MUST be named too.
# * Default arguments may still be omitted.
