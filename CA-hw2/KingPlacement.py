"""
题目：棋盘放置国王 (King Placement)
使用状态压缩动态规划解决棋盘放置国王问题

问题描述：
在 N×N 的棋盘上放置 K 个国王，要求：
1. 同一行内，国王不能相邻
2. 相邻行之间，国王不能互相攻击（包括上下、左上、右上、左下、右下）

输入格式：
第一行：两个整数 N(1 ≤ N ≤ 10) 和 K(0 ≤ K ≤ N²)

输出格式：
输出一个整数，表示满足条件的放置方案数

示例：
输入：
3 2
输出：
16

算法思路：
- 使用状态压缩DP，将每行的放置状态用二进制表示
- dp[k][state] 表示前i行放置k个国王，第i行状态为state的方案数
- 使用滚动数组优化内存空间
"""

try:
    # 读取输入
    N, K = map(int, input().split())
    
    # 生成所有合法行状态
    states = []
    kingCount = []
    
    maxState = 1 << N
    for s in range(maxState):
        # 检查行内是否有相邻的国王
        if s & (s << 1):
            continue
        
        # 计算该状态的国王数量
        count = bin(s).count('1')
        states.append(s)
        kingCount.append(count)
    
    stateCount = len(states)
    
    # 使用二维DP数组优化内存使用
    # dp[i][j] 表示前i行，已放置j个国王的方案数
    dp = [[0] * stateCount for _ in range(K + 1)]
    next_dp = [[0] * stateCount for _ in range(K + 1)]
    
    # 初始化：第0行
    for j in range(stateCount):
        kings = kingCount[j]
        if kings <= K:
            dp[kings][j] = 1
    
    # 逐行处理
    for i in range(1, N):
        # 清空next_dp
        for k in range(K + 1):
            next_dp[k] = [0] * stateCount
        
        for j in range(stateCount):
            currState = states[j]
            currKings = kingCount[j]
            
            for prevJ in range(stateCount):
                prevState = states[prevJ]
                
                # 检查两行状态是否兼容
                if currState & prevState:  # 上下攻击
                    continue
                if currState & (prevState << 1):  # 右上/左下攻击
                    continue
                if (currState << 1) & prevState:  # 左上/右下攻击
                    continue
                
                # 转移状态
                for k in range(currKings, K + 1):
                    if dp[k - currKings][prevJ] > 0:
                        next_dp[k][j] += dp[k - currKings][prevJ]
        
        # 交换dp和next_dp
        dp, next_dp = next_dp, dp
    
    # 统计所有最终状态
    result = 0
    for j in range(stateCount):
        result += dp[K][j]
    
    print(result)

except EOFError:
    exit(0)

