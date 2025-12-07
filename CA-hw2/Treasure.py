"""
问题：Treasure（宝藏）
有界背包问题：给定n个物品，每个物品有价值v、重量w和数量限制m，在总重量不超过W的前提下，求能获得的最大价值。

算法：动态规划 + 二进制优化
- 使用DP数组dp[w]表示总重量为w时能获得的最大价值
- 对于每个物品的多个副本，使用二进制拆分优化（将m个物品拆分为1, 2, 4, ...等2的幂次组合）
- 使用逆序更新DP数组，避免同一物品被重复使用

时间复杂度: O(n * W * log(M))，其中M是最大物品数量
空间复杂度: O(W)

输入格式：
第一行：两个整数 n 和 W，用空格分隔（n为物品数量，W为背包容量）
接下来n行：每行三个整数 v w m，用空格分隔（v为价值，w为重量，m为数量）

输出格式：
输出能获得的最大价值

示例：
输入：
4 20
3 9 3
5 9 1
9 4 2
8 1 3
输出：
47
"""

# 读取第一行
try:
    first_line = input().strip()
    while not first_line:  # 跳过空行
        first_line = input().strip()
    n, W = map(int, first_line.split())
except EOFError:
    print(0)
    exit(0)

# 初始化DP：dp[w] = 总重量为w时能获得的最大价值
dp = [0] * (W + 1)

for _ in range(n):
    try:
        line = input().strip()
        while not line:  # 跳过空行
            line = input().strip()
        v, w, m = map(int, line.split())
    except EOFError:
        break  # 输入不完整，处理剩余部分
    
    # 跳过重量为0的物品
    if w == 0:
        continue
    
    # 有界背包使用二进制优化（拆分为2的幂次）
    k = 1
    remaining = m
    while remaining > 0:
        take = min(k, remaining)
        val = take * v
        wt = take * w
        # 逆序更新DP，避免同一物品被重复使用
        for j in range(W, wt - 1, -1):
            if dp[j - wt] + val > dp[j]:
                dp[j] = dp[j - wt] + val
        remaining -= take
        k *= 2

# 答案是所有重量<=W中的最大价值
print(max(dp))

