from enum import Enum


class Color(Enum):
    red        = 'red'
    crimson    = 'red'
    carmine    = 'red'
    blue       = 'blue'
    aquamarine = 'blue'


"""
we still have unique members, but we now also have aliases.
In fact, our enumeration contains only two members:
"""
print(f"{list(Color) = }") # list(Color) = [<Color.red: 1>, <Color.blue: 2>]
