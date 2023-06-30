import myModule

print(myModule.foo(3))
print(myModule.foo('asdf'))
print(myModule.foo(1.2))
print(myModule.foo([1,2,3]))

from myPackage import module1

module1.func1(123)
module1.func1('asdf')
module1.func1(1.23)
module1.func1([1,2,3])
