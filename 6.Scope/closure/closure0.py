"""
Python Cells and Multi-Scoped Variables
"""

# * Here the value of x is shared between 2 scopes: outer and inner(closure)
# * The label x is in 2 different scopes, but always reference the same "value"
# * Python does this by creating a cell as an intermediary object.
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner
