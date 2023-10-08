# 初始化队列
# 在 Python 中，我们一般将双向队列类 deque 看作队列使用
# 虽然 queue.Queue() 是纯正的队列类，但不太好用，因此不建议

from collections import deque
que = deque()

# 元素入队
que.append(1)
que.append(3)
que.append(2)
que.append(5)
que.append(4)
print("Queue: ", que)

# 访问队首元素
front: int = que[0]
print("Front: ", front)
print("After front: ", que)

# 元素出队
pop: int = que.popleft()
print("Pop: ", pop)
print("After pop: ", que)

# 获取队列的长度
size: int = len(que)
print("Queue length: ", size)

# 判断队列是否为空
is_empty: bool = len(que) == 0
print("Queue is empty: ", is_empty)
