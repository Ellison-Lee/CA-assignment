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

def gen_all_valid(n):
    '''生成所有可能状态'''
    states = []
    def backtrack(pos,curr_state):
        if pos == n:
            states.append(curr_state[:])
            return

        curr_state.append(0) #先全加0
        backtrack(pos+1,curr_state[:])
        curr_state.pop() #撤回加的0，为下一步加1作准备

        if pos == 0 or curr_state[-1]==0: #如果前一位不是0，就加1
            curr_state.append(1)
            backtrack(pos+1,curr_state[:])
            curr_state.pop()#撤回加的0，为下一步加0作准备
    
    backtrack(0,[])
    return states

def is_compatible(pre_state,curr_state):
    '''检查当前行与上一行是否符合规则'''
    for i in range(len(curr_state)):
        if pre_state[i] == 1 and curr_state[i] == 1: #正上方不能有king
            return False
        
        if i>0 and pre_state[i-1] == 1 and curr_state[i] == 1: #左上方不能有king
            return False
        
        if i<len(curr_state)-1 and pre_state[i+1] == 1 and curr_state[i] == 1: #右上方不能有king
            return False

    return True

#读取数据
try:
    n,k = list(map(int,input().split()))
except EOFError:
    exit()

states = gen_all_valid(n) #生成当前所有可用状态
kings_count = [sum(states[i]) for i in range(len(states))] #每个状态放了多少 king
states_count = len(states) #状态数

#初始化第0行dp
dp = [[0]*states_count for _ in range(k+1)] #dp[i][j]表示当前行是j状态，目前所有行一共用了i个king
next_dp = [[0]*states_count for _ in range(k+1)] #下一行的情况，意义同上

for i in range(states_count): #去除掉放了超过k的king的情况
    if kings_count[i] <=k:
        dp[kings_count[i]][i]=1

for row in range(1,n): #正式开始DP，从第一行开始
    next_dp = [[0]*states_count for _ in range(k+1)]  #next_dp清零

    for curr_i in range(states_count): #枚举当前行有效状态
        curr_state = states[curr_i]
        curr_kings = kings_count[curr_i]

        for pre_i in range(states_count): #枚举上一行有效状态
            pre_state = states[pre_i]

            if not is_compatible(pre_state,curr_state): #检查是否匹配
                continue
            
            #状态转移
            for i in range(curr_kings,k+1): 
            #当前行放了用了curr_kings个king，之前行有可能也放了king，所以从current_kings->k遍历
                if dp[i-curr_kings][pre_i] > 0:
                    next_dp[i][curr_i] += dp[i-curr_kings][pre_i]
    
    dp,next_dp = next_dp,dp

#统计总方案数
ans = 0
for i in range(states_count):
    ans += dp[-1][i]

print(ans)