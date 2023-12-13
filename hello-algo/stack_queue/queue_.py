# 初始化队列
# 在 Python 中，我们一般将双向队列类 deque 看作队列使用
# 虽然 queue.Queue() 是纯正的队列类，但不太好用，因此不建议

from collections import deque
que = deque()

# 元素入队
que.append(1)  # 添加至队尾
que.append(3)
que.append(2)
que.append(5)
que.append(4)
que.appendleft(6) # 添加至队首
que.appendleft(7)
print("Queue: ", que)

front: int = que[0]  # 队首元素
rear : int = que[-1] # 队尾元素
print("Front: ", front)
print("Rear : ", rear)
print("After: ", que)

# 元素出队
pop_front = que.popleft() # 队首元素出队
pop_rear  = que.pop()     # 队尾元素出队
print("pop front: ", pop_front)
print("pop rear : ", pop_rear)
print("After pop: ", que)

# 获取队列的长度
size: int = len(que)
print("Queue length: ", size)

# 判断队列是否为空
is_empty: bool = len(que) == 0
print("Queue is empty: ", is_empty)
