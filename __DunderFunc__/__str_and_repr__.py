"""
~ __str__ is used by str() and print() functions.
~ typically used for display purposes to end user, logging, etc
~ if __str__ is not implemented, Python will look for __repr__ instead.

~ __repr__ is used by developers
~ try to make it so that the string could be used to recreated the object.
~ otherwise make it as descriptive as possible.
~ useful for debugging.
~ called when using the repr() function.

~ if neither is implemented and since all objects inherit from Object,
~ will use __repr__ defined there instead
"""

import logging

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'call str. ({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'call repr Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return '{}, {}'.format(self.y, self.x)
        else:
            return '{}, {}'.format(self.x, self.y)

'''
    By default, str() simply calls repr()
    But repr() does not call str()
'''

p = Point2D(123,456)

logging.warning(p)
logging.warning(repr(p))

print(p)
print(repr(p))

'''
    repr() is used when showing elements of a collection
'''
l = [Point2D(i, i*2) for i in range(3)]
print(str(l))
print(repr(l))

'''
    By default, __format__() just calls __str__().
    '{!r}'.format() --- force the use of __repr__()
'''
print('{}'.format(Point2D(1, 2)))
print('{:r}'.format(Point2D(1, 2)))
print('{!r}'.format(Point2D(1, 2)))
print('{!s}'.format(Point2D(1, 2)))
