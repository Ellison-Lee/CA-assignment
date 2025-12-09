"""
题目：棋盘放置国王 (King Placement)
使用动态规划解决棋盘放置国王问题（不使用二进制压缩）

问题描述：
在 N×N 的棋盘上放置 K 个国王，要求：
1. 同一行内，国王不能相邻
2. 相邻行之间，国王不能互相攻击（包括上下、左上、右上、左下、右下）

输入格式：
第一行：两个整数 N和 K

输出格式：
输出一个整数，表示满足条件的放置方案数

示例：
输入：
3 2
输出：
16

算法思路：
- 用列表表示每行的放置状态，例如 [0,1,0] 表示第2个位置有国王
- dp[k][state_idx] 表示前i行放置k个国王，第i行状态为state_idx的方案数
- 使用滚动数组优化内存空间
"""

def generate_valid_states(n):
    """生成所有合法的行状态（行内国王不相邻）"""
    states = []
    
    def backtrack(pos, current_state):
        """递归生成状态"""
        if pos == n:
            states.append(current_state[:])
            return
        
        # 不放国王
        current_state.append(0)
        backtrack(pos + 1, current_state)
        current_state.pop()
        
        # 放国王（前提是前一个位置没有国王）
        if pos == 0 or current_state[-1] == 0:
            current_state.append(1)
            backtrack(pos + 1, current_state)
            current_state.pop()
    
    backtrack(0, [])
    return states

def count_kings(state):
    """计算状态中国王的数量"""
    return sum(state)

def is_compatible(curr_state, prev_state):
    """检查两行状态是否兼容（国王不互相攻击）"""
    n = len(curr_state)
    
    for i in range(n):
        if curr_state[i] == 1 and prev_state[i] == 1:
            # 上下攻击
            return False
        
        if curr_state[i] == 1:
            # 检查左上
            if i > 0 and prev_state[i - 1] == 1:
                return False
            # 检查右上
            if i < n - 1 and prev_state[i + 1] == 1:
                return False
    
    return True

try:
    # 读取输入
    N, K = map(int, input().split())
    
    # 生成所有合法行状态
    states = generate_valid_states(N)
    king_counts = [count_kings(state) for state in states]
    state_count = len(states)
    
    # 使用二维DP数组
    # dp[k][j] 表示已放置k个国王，当前行状态为states[j]的方案数
    dp = [[0] * state_count for _ in range(K + 1)]
    next_dp = [[0] * state_count for _ in range(K + 1)]
    
    # 初始化：第0行
    for j in range(state_count):
        kings = king_counts[j]
        if kings <= K:
            dp[kings][j] = 1
    
    # 逐行处理
    for row in range(1, N):
        # 清空next_dp
        for k in range(K + 1):
            next_dp[k] = [0] * state_count
        
        # 枚举当前行的所有状态
        for curr_j in range(state_count):
            curr_state = states[curr_j]
            curr_kings = king_counts[curr_j]
            
            # 枚举上一行的所有状态
            for prev_j in range(state_count):
                prev_state = states[prev_j]
                
                # 检查两行状态是否兼容
                if not is_compatible(curr_state, prev_state):
                    continue
                
                # 转移状态
                for k in range(curr_kings, K + 1):
                    if dp[k - curr_kings][prev_j] > 0:
                        next_dp[k][curr_j] += dp[k - curr_kings][prev_j]
        
        # 交换dp和next_dp
        dp, next_dp = next_dp, dp
    
    # 统计所有最终状态
    result = 0
    for j in range(state_count):
        result += dp[K][j]
    
    print(result)

except EOFError:
    exit(0)

