###############################################################################
# Unpacking:
# It works with any iterable. Note: set and dict are unordered
###############################################################################

print("========= LHS =========")
lst = [1,2,3,4,5,6]
a, *b = lst     # 等同于: a, b = lst[0], lst[1:]
print(f"a = {a}, b = {b}")

a, *b = (-1, -2, -3, -4)   # always unpacking to a list
print(f"a = {a}, b = {b}") # a = -1, b = [-2, -3, -4]

# ~ The * unpacking operator(means take the rest) can only be used ONCE in the LHS an unpacking assignment
# ~ * operator only unpack the keys of the dictionary.
a, b, *c, d = lst
print(f"a = {a}, b = {b}, c = {c}, d = {d}") # a = 1, b = 2, c = [3, 4, 5], d = 6

a, b, *c, d = 'python'
print(f"a = {a}, b = {b}, c = {c}, d = {d}") # a = p, b = y, c = ['t', 'h', 'o'], d = n


print("========= RHS =========")
l1 = [1,2,3]
l2 = [4,5,6]
print("[*l1, *l2] =", [*l1, *l2]) # [1, 2, 3, 4, 5, 6]
print("[l1, l2] =", [l1, l2])     # [[1, 2, 3], [4, 5, 6]]

l2 = 'XYZ'
print("[*l1, *l2] =", [*l1, *l2]) # [1, 2, 3, 'X', 'Y', 'Z']

# When working with dictionaries, * operator iterated the keys
d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7} # key 'h' in both d2 and d3
print("[*d1, *d2, *d3] =", [*d1, *d2, *d3]) # ['p', 'y', 't', 'h', 'h', 'o', 'n']
print("{*d1, *d2, *d3} =", {*d1, *d2, *d3}) # {'n', 'y', 'h', 'o', 't', 'p'}    Order is NOT guaranteed


print("====== Using ** ======")
# ~ ** unpacking operator CAN NOT be used in the LHS of an assignment
# ~ ** operator unpack the key-values of the dictionary.
d = {**d1, **d2, **d3}
print("{**d1, **d2, **d3} =", d) # {'p': 1, 'y': 2, 't': 3, 'h': 5, 'o': 6, 'n': 7}
                                 # ! 'h' in d3 overwrite the first value of 'h' in d2

d1 = {'a': 1, 'b': 2}
print("{'a': 10, 'c': 3, **d1} =", {'a': 10, 'c': 3, **d1}) # {'a': 1, 'c': 3, 'b': 2}
print("{**d1, 'a': 10, 'c': 3} =", {**d1, 'a': 10, 'c': 3}) # {'a': 10, 'b': 2, 'c': 3}


print("====== Nested Unpacking ======")
a, b, (c, d) = [1, 2, [3, 4]]
print(f"a = {a}, b = {b}, c = {c}, d = {d}") # a = 1, b = 2, c = 3, d = 4

a, *b, (c, d, e) = [1, 2, 3, 'XYZ']
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}") # a = 1, b = [2, 3], c = X, d = Y, e = Z

# Although this looks like we're using * twice in the same expression,
# the second * is actually in a nested unpacking - so that's OK.
# (c, *d) is the last element - 'python'
a, *b, (c, *d) = [1, 2, 3, 'python']
print(f"a = {a}, b = {b}, c = {c}, d = {d}") # a = 1, b = [2, 3], c = p, d = ['y', 't', 'h', 'o', 'n']
