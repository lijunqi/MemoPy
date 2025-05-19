from collections import namedtuple
from typing import Any
from dataclasses import dataclass

Point = namedtuple('AAA', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
# pt3 = Point(3.0) # Error

print(pt1.x, pt1.y)
print(pt2.x, pt2.y)
print(pt1) # AAA(x=1.0, y=5.0)


#######################################

@dataclass
class MyNode:
    val: Any = None
    left: 'MyNode' = None
    right: 'MyNode' = None

    def foo(self):
        return str(self.val) + '_hi'

print(MyNode())
n1 = MyNode(123)
print('n1: ', n1)

n2 = MyNode(123, 'hi')
print('n2: ', n2)
print('call foo: ', n2.foo())

