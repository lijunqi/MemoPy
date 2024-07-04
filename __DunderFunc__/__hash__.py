"""
By default `__hash__` uses the object's identity,
and `__eq__` will only evaluate to `True` if the two objects are the same objects (identity).
"""
class Person:
    def __init__(self, name):
        self.name = name

    # * If we override the `__eq__` method, Python will automatically make our class unhashable:
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


p1 = Person("Jacky")
d = {p1: 'person 1'}
print("p1: ", d[p1])
