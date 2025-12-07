"""
问题2: 逆序对计数 (Inversion Count)
题目：给定一个数组，计算数组中逆序对的数量
逆序对定义：如果 i < j 且 arr[i] > arr[j]，则 (i, j) 是一个逆序对

算法：使用归并排序计算逆序对数量
- 在归并过程中，如果右半部分的元素小于左半部分的元素
- 则说明该右半部分元素与左半部分剩余的所有元素都构成逆序对

时间复杂度: O(n log n)

输入格式：
第一行：测试用例数量 T
对于每个测试用例：
  第一行：数组长度 n
  第二行：n 个整数，用空格分隔

输出格式：
对于每个测试用例，输出逆序对的数量

示例：
输入：
1
5
5 2 3 4 1
输出：
10
"""


# 合并并统计逆序对数量
def merge_and_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    # 复制到临时数组
    for idx in range(left, right + 1):
        temp[idx] = arr[idx]
    
    # 合并两个有序子数组并统计逆序对
    while i <= mid and j <= right:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
            k += 1
        else:
            arr[k] = temp[j]
            j += 1
            k += 1
            # 左半部分剩余元素都与当前右元素构成逆序对
            inv_count += (mid - i + 1)
    
    # 复制左半部分剩余元素
    while i <= mid:
        arr[k] = temp[i]
        i += 1
        k += 1
    # 右半部分剩余元素无需处理（已在原数组）
    
    return inv_count


# 归并排序并统计逆序对总数
def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = left + (right - left) // 2  # 避免溢出
        
        # 分治处理左右子数组
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        # 合并并统计当前层逆序对
        inv_count += merge_and_count(arr, temp, left, mid, right)
    return inv_count


# 读取输入
try:
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        temp = [0] * n  # 临时数组，避免重复分配
        
        # 计算逆序对总数
        result = merge_sort_and_count(arr, temp, 0, n - 1)
        print(result)
except EOFError:
    exit()
