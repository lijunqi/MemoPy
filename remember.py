g_cnt = 1
print('########################### %d ###########################' % g_cnt)
import json
print(json.loads('[1,2,3]'))

g_cnt = 2
print('########################### %d ###########################' % g_cnt)
a = [1,2,3]
for idx, val in enumerate(a):
    print(idx, val)

g_cnt = 3
print('########################### %d ###########################' % g_cnt)
print('123 % 10 = ', 123 % 10)
print('123 // 10 = ', 123 // 10)

g_cnt = 4
print('########################### %d ###########################' % g_cnt)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Deep First Search
def rserialize(root, s):
    if root is None:
        s += 'null,'
    else:
        s += str(root.val) + ','
        s = rserialize(root.left, s)
        s = rserialize(root.right, s)
    return s

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(5)
l = rserialize(t, '')
print(l)

# ! ! ! str don't have pop()
def rdeserialize(lst):
    if len(lst) == 0 or lst[0] == 'null':
        del(lst[0])
        return None

    root = TreeNode(lst[0])
    del(lst[0])
    root.left = rdeserialize(lst)
    root.right = rdeserialize(lst)
    return root

r = rdeserialize(l.split(','))
print(r.val)
print(r.left.val)
print(r.right.val)
#print(r.left.left.val)
#print(r.left.right.val)
print(r.right.left.val)
print(r.right.right.val)


g_cnt = 5
print('########################### %d ###########################' % g_cnt)
# checks whether the string consists of alphanumeric characters
# --- isdigit(), isalpha() ---
str = "runoob2016"
print (str.isalnum()) # True
 
str = "www.runoob.com"
print (str.isalnum()) # False

def isPalindrome(s: str) -> bool:
    # Best ans:
    sgood = "".join(ch.lower() for ch in s if ch.isalnum())
    return sgood == sgood[::-1]


g_cnt = 6
print('########################### %d ###########################' % g_cnt)
print( (5>>1) == int(5/2) )


g_cnt = 7
print('########################### %d ###########################' % g_cnt)
print(int('11', 2))    # 3 binary --> decimal
print(int('0xfF', 16)) # 255
print(list(range(5, 0, -1)))


g_cnt = 8
print('########################### %d ###########################' % g_cnt)
a = [3,2,3,1,2,4,5,5,6]
s = sorted(a, reverse=True)
print(s)
