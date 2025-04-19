
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

if __name__ == "__main__":
    mylist = [1,2,3]
    flag = 3
    #func1(mylist, flag)
    func2(mylist, flag)

    flag = 4
    #func1(mylist, flag)
    func2(mylist, flag)
