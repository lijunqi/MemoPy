"""
~ Filter #############################################################################
! filter(func, iterable)
! It allow us to specify a function that determines wheter we retain or throw out
! the elements of that iterable.
func takes a single argument, retain if it return true, throw if it return false.
* If the function is None, it returns the elements of iterable that are Truthy.
"""
l = [0, 1, 2, 3, 4]
print(list(filter(None, l))) # [1, 2, 3, 4]

def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, l))) # [0, 2, 4]
