"""
问题4: 最大子数组和 (Maximum Subarray Sum)
使用Kadane算法计算数组的最大子数组和
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


def max_subarray_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # current_max: 以当前位置结尾的最大子数组和
    # global_max: 全局最大子数组和
    current_max = 0
    global_max = 0
    
    for num in arr:
        # 要么将当前数字加入现有子数组，要么从当前数字开始新的子数组
        current_max = max(0, current_max + num)
        # 更新全局最大值
        global_max = max(global_max, current_max)
    
    return global_max

# 读取输入
try:
    n = int(input())
    arr = list(map(int, input().split()))
except EOFError:
    exit()

# 计算并输出结果
result = max_subarray_sum(arr)
print(result)