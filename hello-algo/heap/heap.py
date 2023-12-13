import heapq
"""
堆作为完全二叉树的一个特例，具有以下特性。
    1. 最底层节点靠左填充，其他层的节点都被填满。
    2. 我们将二叉树的根节点称为“堆顶”，将底层最靠右的节点称为“堆底”。
    3. 对于大顶堆（小顶堆），堆顶元素（即根节点）的值分别是最大（最小）的。

堆通常用作实现优先队列(priority queue)，大顶堆相当于元素按从大到小顺序出队的优先队列

采用数组来存储堆: 给定索引i, 其左子节点为(2*i + 1), 右子节点: (2*i + 2), 父节点: (i-1)/2 向下取整
当索引越界时，表示空节点或节点不存在。

入堆: 我们比较插入节点与其父节点的值, 如果插入节点更大, 插入节点上升(将它们交换).
然后继续执行此操作, 从底至顶修复堆中的各个节点, 直至越过根节点或遇到无须交换的节点时结束

堆顶元素出堆:
    1. 交换堆顶元素与堆底元素(即交换根节点与最右叶节点).
    2. 交换完成后, 将堆底从列表中删除(注意, 由于已经交换, 实际上删除的是原来的堆顶元素).
    3. 从根节点开始, 从顶至底执行堆化: 我们将根节点的值与其两个子节点的值进行比较, 将最大的子节点与根节点交换.
       然后循环执行此操作, 直到越过叶节点或遇到无须交换的节点时结束
"""

# 初始化小顶堆
min_heap, flag = [], 1
# 初始化大顶堆
max_heap, flag = [], -1

# Python 的 heapq 模块默认实现小顶堆
# 考虑将“元素取负”后再入堆，这样就可以将大小关系颠倒，从而实现大顶堆
# 在本示例中，flag = 1 时对应小顶堆，flag = -1 时对应大顶堆

# * 元素入堆
heapq.heappush(max_heap, flag * 1)
heapq.heappush(max_heap, flag * 3)
heapq.heappush(max_heap, flag * 2)
heapq.heappush(max_heap, flag * 5)
heapq.heappush(max_heap, flag * 4)

# 获取堆顶元素
peek = flag * max_heap[0] # 5
print("Max_heap: ", max_heap)

# 堆顶元素出堆
# 出堆元素会形成一个从大到小的序列
val = flag * heapq.heappop(max_heap); print(val) # 5
val = flag * heapq.heappop(max_heap); print(val) # 4
val = flag * heapq.heappop(max_heap); print(val) # 3
val = flag * heapq.heappop(max_heap); print(val) # 2
val = flag * heapq.heappop(max_heap); print(val) # 1

# 获取堆大小
size = len(max_heap)

# 判断堆是否为空
is_empty = not max_heap

# * 输入列表并建堆
min_heap = [1, 5, 4, 3, 2]
heapq.heapify(min_heap)
print("Min heap:", min_heap)
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
