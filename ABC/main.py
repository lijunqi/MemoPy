from abc import ABC

class MyBase:
    def __init__(self, data) -> None:
        self.data = data

    #def __new__(cls, *args, **kwargs):
    #    if cls is MyBase:
    #        raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
    #    return object.__new__(cls, *args, **kwargs)


class A(MyBase):
    def __init__(self, data) -> None:
        super().__init__(data)

class B(A):
    def __init__(self, data) -> None:
        super().__init__(data)


def main():
    # * 1
    a = A(456)
    print(f"a is instance of MyBase: {isinstance(a, MyBase)}") # True
    
    # * 2
    b = B(789)
    print(f"b is instance of MyBase: {isinstance(b, MyBase)}") # True
    print(f"b is instance of A: {isinstance(b, A)}") # True
    print(f"b is instance of B: {isinstance(b, B)}") # True
    print(f"type(a) == A: {type(a) == A}") # True
    print(f"type(b) == B: {type(b) == B}") # True

    print("-------------------------------------")
    print(f"type(a) == MyBase: {type(a) == MyBase}") # False
    print(f"type(b) == MyBase: {type(b) == MyBase}") # False
    print(f"type(b) == A: {type(b) == A}") # False



    # * 3

if __name__ == "__main__":
    main()
