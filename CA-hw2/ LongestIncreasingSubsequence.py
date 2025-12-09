"""
问题：Longest Increasing Subsequence（最长递增子序列）
给定一个长度为n的整数序列，求其最长递增子序列（LIS）的长度。

算法：贪心 + 二分查找
- 维护一个数组tails，其中tails[i]表示长度为i+1的递增子序列的最小末尾元素
- 对于每个元素，使用二分查找找到它在tails中的位置
- 如果元素大于所有现有末尾元素，则扩展最长子序列
- 否则，更新对应长度的最小末尾元素

时间复杂度: O(n log n)
空间复杂度: O(n)

输入：
8
10 9 2 5 3 7 101 18
输出：
4
"""

# 读取输入
try:
    # 读取第一行（n的值）
    n_line = input().strip()
    while not n_line:  # 跳过空行
        n_line = input().strip()
    n = int(n_line)
    
    # 读取第二行（序列）
    nums_line = input().strip()
    while not nums_line:  # 跳过空行
        nums_line = input().strip()
    nums = list(map(int, nums_line.split()))

except EOFError:
    exit(0)

tails = []
for num in nums:
    # 手动二分查找：找到第一个 >= num 的位置
    left, right = 0, len(tails)
    while left < right:
        mid = (left + right) // 2
        if tails[mid] < num:
            left = mid + 1
        else: #找到目标位置
            right = mid 
    if left == len(tails): #如果找不到目标位置，则添加到末尾
        tails.append(num)
    else:
        tails[left] = num #如果找到目标位置，则更新该位置的值

print(len(tails))