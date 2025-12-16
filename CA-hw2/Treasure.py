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
try:
    n,total_w = list(map(int,input().split()))
    dp = [0]*(total_w+1) #dp[i]是最大容量为i时，包内的最大价值

    for _ in range(n): #按照每种物品开始dp
        v,w,m = list(map(int,input().split()))
        k = 1 #准备取的物品数量
        remaining = m #当前剩余数量

        while remaining > 0:
            take = min(remaining,k) #避免多拿
            val = take*v
            wt = take*w
            for i in range(total_w,wt-1,-1):
                if dp[i-wt]+val > dp[i]: #状态转移：如果拿当前物品比已有的dp[i]的价值还大，就更新
                    dp[i] = dp[i-wt]+val
            remaining -= take
            k *=2 #每次取物翻倍
    print(max(dp))
except EOFError:
    exit()
    