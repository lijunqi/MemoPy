
class A:
    class_var = 123
    def __init__(self, name, ip) -> None:
        self.a = 1
        self.b = "hello"
        self.c = {
            "name": "kaka",
            "age": 10
        }
        self.d = Result(name, ip)
    
    def foo(self):
        return self.a, self.b

class Result:
    def __init__(self, name, ip) -> None:
        self.name = name
        self.ip = ip

a = A("kuku", "123.456")
print("a dict: ", a.__dict__)
# Output: no class member "class_var"
# {'a': 1, 'b': 'hello', 'c': {'name': 'kaka', 'age': 10}, 'd': <__main__.Result object at 0x01CA63F0>}

print("A dict: ", A.__dict__)
print("a.a = ", getattr(a, 'a'))
print("a.b = ", getattr(a, 'b'))
c = getattr(a, 'c')
print("a.c = ", c)
print("type a.c = ", type(c))

d = getattr(a, 'd')
print("d.name = ", getattr(d, 'name'))
print("type a.d = ", type(d))


####################################################
""" 我们需要获取传入的字典的各个键值，并创建键值同名一个属性 """
class B:
    def __init__(self, data) -> None:
        self.data = data

class MyClass:
    def __init__(self, params: dict) -> None:
        self.__dict__.update(params)
        print("Myclass dict: ", self.__dict__)

params = {
    "name": "xxx",
    "timeout_s": 120,
    "x1": "abc",
    "x2": B(456)
}
myc = MyClass(params)
print("myc.name =", myc.name)
print("myc.timeout_s =", myc.timeout_s)
print("myc.x1 =", myc.x1)
print("myc.x2 =", myc.x2)
print("myc.x2.data =", myc.x2.data)
print("Does myc has attribute x3? ", hasattr(myc, "x3"))
print("myc.x3 =", getattr(myc, "x3", None))
