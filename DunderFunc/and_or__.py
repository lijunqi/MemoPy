"""
The magic methods __and__, __or__ and __invert__ are used to override the operators a & b, a | b and ~a respectively. 
"""

class A():
    def __init__(self, check: bool) -> None:
        self.check = check

    def __and__(self, other):
        print("Here is and")
        return self.check and other.check

    def __or__(self, other):
        print("Here is or")
        return self.check or other.check
    
    def __invert__(self):
        print("Here is invert")
        return not self.check


a1 = A(True)
a2 = A(False)
a3 = A(True)

print(a1 & a2)
print(a1 & a3)

print("=========")
print(a1 | a2)
print(a1 | a3)

print("=========")
print(~a1)
