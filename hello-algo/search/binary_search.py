""" 
二分查找(binary search)是一种基于分治策略的高效搜索算法。
它利用数据的 有序性，每轮减少一半搜索范围，直至找到目标元素或搜索区间为空为止

* 二分查找仅适用于有序数据, 数组
* 小数据量下，线性查找性能更佳

如果i+j溢出, 使用 m = math.floor( i + (j-i)/2 )
"""

def binary_search(nums: list[int], target: int) -> int:
    """二分查找（双闭区间）"""
    # ! 初始化双闭区间 [0, n-1], 即i, j分别指向数组 首尾元素
    i, j = 0, len(nums) - 1
    # 循环，当搜索区间为空时跳出（当 i > j 时为空）
    while i <= j:
        # 理论上 Python 的数字可以无限大（取决于内存大小），无须考虑大数越界问题
        m = (i + j) // 2  # ! 中点索引 m 向下取整
        if nums[m] < target:
            i = m + 1  # 说明 target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # 说明 target 在区间 [i, m-1] 中
        else:
            return m  # 找到目标元素，返回其索引
    return -1  # 未找到目标元素，返回 -1

nums = [1,3,6,8,12,15,23,26,31,35]
print(binary_search(nums, 6))

