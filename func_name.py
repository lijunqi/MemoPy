#coding=utf-8 
import sys 
import inspect 

# Get current function name: sys._getframe().f_code.co_name

def my_name():
    print('1' , sys._getframe().f_code.co_name)
    print('2' , inspect.stack()[0][3])
  
def get_current_function_name():
    print('5', sys._getframe().f_code.co_name)
    return inspect.stack()[1][3] 

class MyClass:
    def function_one(self):
        print('3', inspect.stack()[0][3])
        print('4', sys._getframe().f_code.co_name)
        print("6 %s.%s invoked" % (self.__class__.__name__,
                get_current_function_name()) )
        print(inspect.stack())
  
if __name__ == '__main__':
    my_name()
    myclass = MyClass()
    myclass.function_one()

# Output:
# 1 my_name
# 2 my_name
# 3 function_one
# 4 function_one
# 5 get_current_function_name
# 6 MyClass.function_one invoked
