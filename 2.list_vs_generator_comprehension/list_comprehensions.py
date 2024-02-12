
# equals
# >>> squares = []
# >>> for x in range(10):
# ...     squares.append(x**2)
# Note that this creates (or overwrites) a variable named x that still exists after the loop completes.

squares = list(map(lambda x: x**2, range(10)))
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# A list comprehension consists of brackets containing an expression
# followed by a for clause, then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression
# in the context of the for and if clauses which follow it.
# For example, this listcomp combines the elements of two lists if they are not equal.
# it's equivalent to:
# >>> combs = []
# >>> for x in [1,2,3]:
# ...     for y in [3,1,4]:
# ...         if x != y:
# ...             combs.append((x, y))

diff = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(diff)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
flatten = [num for ele in vec for num in ele]
print(flatten) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


####################################
###  Nested List Comprehensions  ###
####################################
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
nest = [[row[i] for row in matrix] for i in range(4)]
print(nest) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# is equivalent to:
# >>> transposed = []
# >>> for i in range(4):
# ...     transposed.append([row[i] for row in matrix])


# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for this use case:
print(list(zip(*matrix))) # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
