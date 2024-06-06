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
    if isinstance(a, MyBase):
        print("a is instance of MyBase.")
    
    if type(a) == MyBase:
        print("type(a) == MyBase")
    else:
        print("type(a) != MyBase")

    # * 2
    b = B(789)
    if isinstance(b, MyBase):
        print("b is instance of MyBase.")
    if isinstance(b, A):
        print("b is instance of A.")
    if isinstance(b, B):
        print("b is instance of B.")

    if type(b) == MyBase:
        print("type(b) == MyBase")
    else:
        print("type(b) != MyBase")

    if type(b) == A:
        print("type(b) == A")
    else:
        print("type(b) != A")

    if type(b) == B:
        print("type(b) == B")
    else:
        print("type(b) != B")

    # * 3

if __name__ == "__main__":
    main()
