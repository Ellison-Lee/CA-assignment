"""
问题4: 最大子数组和 (Maximum Subarray Sum)
维护global max,current max
时间复杂度: O(n)

输入格式：
第一行：数组长度 n
第二行：n 个整数，用空格分隔

输出格式：
输出最大子数组和

示例：
输入：
9
-2 1 -3 4 -1 2 1 -5 4
输出：
6
"""
#读取数据
try:
    n = int(input())
    arr = list(map(int,input().split()))
except EOFError:
    exit()

c_max = 0 #当前最大值
g_max = 0 #全局最大值

for num in arr:
    c_max = max(0,c_max+num) #如果当前数组和为负，则从下一个数重新开始
    g_max = max(c_max,g_max)

print(g_max)
