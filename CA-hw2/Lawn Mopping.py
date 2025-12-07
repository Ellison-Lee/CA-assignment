"""
问题：Lawn Mopping（草坪拖地）
给定一个长度为n的数组，选择一些元素使得任意两个被选元素之间的距离不超过k，求所选元素的最大和。

算法：动态规划 + 单调队列优化
- 使用DP数组dp[i]表示考虑前i个元素，且第i个位置不选时的最大和
- 使用单调队列维护滑动窗口内的最优决策位置
- 通过前缀和优化区间和的计算

时间复杂度: O(n)
空间复杂度: O(n)

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
    # 读取输入
    n, k = map(int, input().split())
    
    # 特殊情况处理
    if n == 0:
        print(0)
    
    # 读取所有元素并计算前缀和
    prefix = [0] * (n + 2)
    for i in range(1, n + 1):
        x = int(input())
        prefix[i] = prefix[i - 1] + x
    
    # 特殊情况：如果k>=n，选择所有正数
    if k >= n:
        sum_val = 0
        for i in range(1, n + 1):
            val = prefix[i] - prefix[i - 1]
            if val > 0:
                sum_val += val
        print(sum_val)
    
    # DP数组：dp[i]表示考虑前i个元素，且第i个位置不选时的最大和
    dp = [0] * (n + 2)
    dq = deque()
    
    # 初始化：位置0作为起始断点
    dq.append(0)
    dp[0] = 0
    
    # 核心迭代过程
    for i in range(1, n + 2):
        # 步骤A - 窗口维护：移除超出窗口范围的位置
        while dq and dq[0] < i - k - 1:
            dq.popleft()
        
        # 步骤B - 最优决策
        if dq:
            j = dq[0]
            # 状态转移：前j个元素的最优解 + j到i-1位置的元素和
            dp[i] = dp[j] + (prefix[i - 1] - prefix[j])
        
        # 步骤C - 队列更新
        # 从尾部移除所有不如当前位置i优的候选位置
        while dq:
            last = dq[-1]
            # 比较标准：dp[last] - prefix[last] <= dp[i] - prefix[i]
            if dp[last] - prefix[last] <= dp[i] - prefix[i]:
                dq.pop()
            else:
                break
        dq.append(i)
    
    # 输出最终结果
    print(dp[n + 1])
except EOFError:
    exit(0)


