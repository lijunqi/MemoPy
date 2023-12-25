
def binary_search_insertion(nums: list[int], target: int) -> int:
    """二分查找插入点（存在重复元素）"""
    i, j = 0, len(nums) - 1  # 初始化双闭区间 [0, n-1]
    while i <= j:
        m = (i + j) // 2  # 计算中点索引 m
        print("i = %d, j = %d, m = %d, nums[m] = %d" % (i, j, m, nums[m]))
        if nums[m] < target:
            i = m + 1  # target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # target 在区间 [i, m-1] 中
        else:
            j = m - 1  # 首个小于 target 的元素在区间 [i, m-1] 中
    # 返回插入点 i
    print("Last: i = %d, j = %d" % (i, j))
    return i

nums = [1,3,4,5,6,6,6,10,12,15]
print("Nums: ", nums)
print(binary_search_insertion(nums, 6))

nums = [1,3,6,6,6,6,6,10,12,15]
print("Nums: ", nums)
print(binary_search_insertion(nums, 6))