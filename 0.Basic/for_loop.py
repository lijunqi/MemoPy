
#%%
def func1(mylist, flag):
    found = False
    for i in mylist:
        if i == flag:
            found = True
            break

    if found:
        print("Func1 find it.")
    else:
        print("Func1 not find it.")

def func2(mylist, flag):
    for i in mylist:
        if i == flag:
            print("Func2 find it.")
            break
    else:
        print("Func2 not find it.")

my_list = [1,2,3]
flag = 3
#func1(my_list, flag)
func2(my_list, flag)

flag = 4
#func1(my_list, flag)
func2(my_list, flag)


#%%
"""
In this example:
If search_value is found, the break statement prevents the else block from executing.
If search_value is not found, the loop completes normally, and the "not found" message is printed by the else block
"""
items = [1, 2, 3, 4, 5]
def for_else(items, search_value):
    for item in items:
        if item == search_value:
            print(f"{search_value} found!")
            break
    else:
        print(f"{search_value} not found in the list.")

# * for else
for_else(items, 5)
for_else(items, 6)

#%%
def for_else_no_break(items, search_value):
    for item in items:
        if item == search_value:
            print(f"{search_value} found!")
    else:
        print(f"{search_value} not found in the list. (else block executed)")

for_else_no_break(items, 5)
for_else_no_break(items, 6)
