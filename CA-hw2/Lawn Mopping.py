"""
问题：Lawn Mopping（草坪拖地）
给定一个长度为n的数组，不能连续选择k个元素，求所选元素的最大和。

算法：动态规划 + 单调队列优化
- 使用DP数组max_sum[i]表示考虑前i个元素，且第i个位置不选时的最大和
- 使用单调队列维护滑动窗口内的最优决策位置
- 通过前缀和优化区间和的计算

时间复杂度: O(n)

输入格式：
第一行：两个整数 n 和 k，用空格分隔
接下来n行：每行一个整数，表示数组元素

输出格式：
输出所选元素的最大和

示例：
输入：
5 2
1
2
3
4
5
输出：
12
"""
from collections import deque

try:
    n,k = list(map(int,input().split()))
    prefix = [0]*(n+2) #开始前，结束后有默认的2个隐形断点，所以prefix也有n+2个元素
    for i in range(1,n+1):
        x = int(input())
        prefix[i] = prefix[i-1]+x #计算前缀和
except EOFError:
    exit()

max_sum = [0]*(n+2) #开始前，结束后有默认的2个隐形断点
breakpoint = deque()
breakpoint.append(0) #第0个元素当作断点

for i in range(1,n+2):
    while breakpoint[0] < i-k-1: #维护有效断点的窗口，两个断点相距k个元素
        breakpoint.popleft()

    if breakpoint:
        j = breakpoint[0]
        max_sum[i] = max_sum[j] + prefix[i-1]-prefix[j] #max_sum[i]表示第i个元素当断点时，[1:i]数组的最大和

    while breakpoint:
        last = breakpoint[-1]
        if max_sum[last]-prefix[last] <= max_sum[i]-prefix[i]: #淘汰非最优的断点
            breakpoint.pop()
        else:
            break
        
    breakpoint.append(i)

print(max_sum[n+1])
