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