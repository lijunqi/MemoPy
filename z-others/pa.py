
class MyClass:
    def __init__(self) -> None:
        self.__secret = 123

o = MyClass()
#print(o.__secret)
# name mangling
print("secret is ", o._MyClass__secret)
