""" Optimization """

# * ====== Pre-calculate const value ======
def func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox123' * 5 # ! more than 20 characters
    f = ['a', 'b'] * 3
print("func co_consts: ", func.__code__.co_consts)

def my_func(e):
    if e in [1,2,3]:
        pass
print("co_consts: ", my_func.__code__.co_consts)


# * ====== Set is faster ======
import time
import string
print("ascii: ", string.ascii_letters)
char_list = list(string.ascii_letters)
char_tuple  = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    start = time.perf_counter()
    for i in range(n):
        if 'z' in container:
            pass
    print("perf: ", time.perf_counter() - start)

membership_test(10000000, char_list)  # list : 3.5s
membership_test(10000000, char_tuple) # tuple: 3.3s
membership_test(10000000, char_set)   # * set: 0.5s
