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

#读取输入
try:
    n = int(input())
    arr = list(map(int,input().split()))
except EOFError:
    exit()

tail = []

for num in arr: 
    #二分查找tail数组种第一个 > num的位置
    left,right = 0,len(tail)
    mid = (left+right)//2

    while left < right:
        if tail[mid] < num:
            left = mid +1
            mid = (left+right)//2
        elif tail[mid] >= num: 
            right = mid #mid有可能就是目标位置，所以设置 right=mid
            mid = (left+right)//2
    
    if left == len(tail): #如果num大于所有tail，说明递增数组可以扩大
        tail.append(num) 
    else:
        tail[left] = num #找到left长度有更小的末尾元素

print(len(tail))

        


