
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = ", list1)
print("list2 = ", list2)
print("list3 = ", list3)

"""
Result:
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
"""

def extendList2(val, list=None):
    if list is None:
        list = []
        list.append(val)
    return list

list4 = extendList2(10)
list5 = extendList2(123,[])
list6 = extendList2('a')

print("list4 = ", list4)
print("list5 = ", list5)
print("list6 = ", list6)

"""
Result:
list4 =  [10]
list5 =  []
list6 =  ['a']
"""
