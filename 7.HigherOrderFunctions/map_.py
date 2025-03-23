"""
~ Map ################################################################################
! map function
"""
l = [2, 3, 4]
def sq(x):
    return x**2

print(list(map(sq, l))) # [4, 9, 16]


l1 = [1, 2, 3]
l2 = [10, 20, 30]

def add(x, y):
    return x + y

# * If we had uneven length lists over here, it would stop at the shortest length.
print(list(map(add, l1, l2))) # [11, 22, 33]
