
class MyClass:
    def __init__(self) -> None:
        self.__secret = 123

o = MyClass()
#print(o.__secret)
# name mangling
print(o._MyClass__secret)
