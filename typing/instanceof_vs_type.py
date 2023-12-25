
print(isinstance(2, int)) # True

print(isinstance(2, str)) # False

print(isinstance(2, (str, int, list))) # True

class A:
    pass

class B(A):
    pass

class C(B):
    pass

inst_a = A()
inst_b = B()
inst_c = C()

print("type(inst_a) == A", type(inst_a) == A) # True
print("type(inst_b) == A", type(inst_b) == A) # False
print("type(inst_c) == A", type(inst_c) == A) # False


print("isinstance(inst_a, A)", isinstance(inst_a, A)) # True
print("isinstance(inst_b, A)", isinstance(inst_b, A)) # True
print("isinstance(inst_c, A)", isinstance(inst_c, A)) # True
print("isinstance(inst_c, B)", isinstance(inst_c, B)) # True
print("isinstance(inst_c, C)", isinstance(inst_c, C)) # True
