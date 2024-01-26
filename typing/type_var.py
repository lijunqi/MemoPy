""" mypy . """
import typing as t


# * #####################
# * 类型别名:
# * 是使用 type 语句来定义的，它将创建一个 TypeAliasType 的实例.
# * 在这个示例中，Vector 和 list[float] 将被静态类型检查器等同处理
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print("New vector:", new_vector)


# * #####################
# * 类型变量:
# * 用于创建表示不确定类型的占位符
T = t.TypeVar('T', int, str)

def foo(x: T) -> None:
    print('x = ', x)

foo(1)
foo("123")
#! foo([1,2,3]) # error: Value of type variable "T" of "foo" cannot be "List[int]"  [type-var]

num1: T = 1
num2: T = "456"
num3: T = [4,5,6]
print(num1)
print(num2)
print(num3)
print(t.TYPE_CHECKING)

# * Using type variables as parameters
def remove_falsey_from_list(items: list[T]) -> list[T]:
    return [item for item in items if item]

# * #####################
# * 函数: 或其他 callable 对象
# * 可以使用 collections.abc.Callable 或 typing.Callable 来标注.
# * Callable[[int], str] 表示一个接受 int 类型的单个参数并返回 str 的函数.


# * #####################
# * 联合类型: typing.Union
# * Union[X, Y] 等价于 X | Y ，意味着满足 X 或 Y 之一.


# * #####################
# 用 C 注解的变量可以接受类型 C 的值.
# 然而，用类型 type[C] （或者 typing.Type[C] ）注解的变量则可以接受本身是类的值
# 准确地说，是接受 C 的 类对象
# type[Any] 等价于 type
class User: ...
class ProUser(User): ...
class TeamUser(User): ...

def make_new_user(user_class: type[User]) -> User:
    # ...
    return user_class()

make_new_user(User)      # OK
make_new_user(ProUser)   # Also OK: ``type[ProUser]`` is a subtype of ``type[User]``
make_new_user(TeamUser)  # Still fine
make_new_user(User())    # Error: expected ``type[User]`` but got ``User``
make_new_user(int)       # Error: ``type[int]`` is not a subtype of ``type[User]``


import math

C = t.TypeVar('C', bound='Circle')

class Circle:
    """An abstract circle"""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    # Use a type variable to show that the return type
    # will always be an instance of whatever ``cls`` is
    @classmethod
    def with_circumference(cls: type[C], circumference: float) -> C:
        """Create a circle with the specified circumference"""
        radius = circumference / (math.pi * 2)
        return cls(radius)


class Tire(Circle):
    """A specialised circle (made out of rubber)"""

    MATERIAL = 'rubber'


c = Circle.with_circumference(3)  # Ok, variable 'c' has type 'Circle'
t = Tire.with_circumference(4)  # Ok, variable 't' has type 'Tire' (not 'Circle')