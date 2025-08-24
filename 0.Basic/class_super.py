
"""
super(cls, inst):
    mro = inst.__class__mro()
    return mro(mro.index(cls) + 1)
"""

class BaseClass(object):
    def __init__(self) -> None:
        print('Enter BaseClass')
        print('Leave BaseClass')

class A(BaseClass):
    def __init__(self) -> None:
        print('Enter A')
        super().__init__() # Equal to: super(A, self).__init__()
        print('Leave A')

class B(BaseClass):
    def __init__(self) -> None:
        print('Enter B')
        super().__init__()
        print('Leave B')

class C(B, A):
    def __init__(self) -> None:
        print('Enter C')
        super().__init__()
        print('Leave C')

c = C()
print("C's MRO: ", C.__mro__)
super(B, c).__init__()
