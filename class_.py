# coding=utf-8

class Teacher():
    def __init__(self,name,level):
      self.__name = name
      self.__level = level
  
    # 获取老师的等级
    def get_level(self):
      return self.__level
  
    # 获取名字
    def get_in_name(self):
      return self.__name

    def set_name(self, name):
        self.__name = name



# 定义动态方法
def get_name(self):
    return self.__name


# 动态方法赋值
Teacher.get_name = get_name
t = Teacher("GG",5)
print("level is: ", t.get_level())  # 可行
#print("name is ", t.__name)        # error. no attribute
#print("name is ", t.get_name())    # 报错，显示没有该属性

t.set_name("NN")
print(t.get_in_name())


print("name is",t._Teacher__name)   # 输出GG
t._Teacher__name="AA"               # 被改变了
print("name is",t._Teacher__name)   # 输出AA


class Parent(object):
    def __init__(self):
        self._data = "data in parent"

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

ch = Child()
print(ch._data)

