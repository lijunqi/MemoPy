"""
~ Zip ################################################################################
! zip(*iterables): takes in multiple iterables and return 1 iterable.
! It's not a higher order function
"""
l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = ['a', 'b', 'c']
zip_obj = zip(l1, l2, l3)
print(list(zip_obj)) # [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]

# * stop at the shorest length
l4 = [1, 2, 3]
l5 = [10, 20, 30, 40]
l6 = 'python'
print(list(zip(l4, l5, l6))) # [(1, 10, 'p'), (2, 20, 'y'), (3, 30, 't')]
