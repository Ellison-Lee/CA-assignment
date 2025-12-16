"""
Chat Program - 最大化第k大元素

问题描述：
给定一个整数序列，可以选择一个连续子数组，将等差数列加到该子数组上。
目标是最大化操作后序列中第k大的元素。

算法思路：
1. 枚举所有可能的子数组起始位置（包括不执行操作）
2. 对每个位置，执行操作并计算第k大元素
3. 返回所有可能结果中的最大值

时间复杂度：O(n² log n)

输入：
6 4 3 1 2
1 1 4 5 1 4
输出：
4
"""
def find_kth(k,arr):
    temp = sorted(arr,reverse=True) #temp.sort()是在原数组排序，temp=sorted()则不会
    return temp[k-1]

try:
    n,k,m,c,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    ar_seq = [c+i*d for i in range(m)]
    kth = find_kth(k,arr)

    for i in range(n-m+1):
        temp = arr[:] 
        for j in range(m):
            temp[i+j] += ar_seq[j]
        curr_kth = find_kth(k,temp)
        kth = max(kth,curr_kth)

    print(kth)
except EOFError:
    exit()