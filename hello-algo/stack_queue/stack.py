# 初始化栈
# Python 没有内置的栈类，可以把 List 当作栈来使用 
stack = []

# 元素入栈
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)
print("stack: ", stack)

# 访问栈顶元素
peek: int = stack[-1]
print("peek: ", peek)
print("After peek: ", stack)

# 元素出栈
pop: int = stack.pop()
print("pop: ", pop)
print("After pop: ", stack)

# 获取栈的长度
size: int = len(stack)
print("Stack length: ", size)

# 判断是否为空
is_empty: bool = len(stack) == 0
print("Stack is empty: ", is_empty)
