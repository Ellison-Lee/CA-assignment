"""
问题: K Co-prime Permutation
构造一个排列，使得恰好有k个位置i满足gcd(p_i, i) = 1

输入：
5 3
输出：
1 4 5 2 3

"""
try:
    n, k = map(int, input().split())

    if k == 0:
        print(-1)
    else:
        # 先输出k，再按顺序输出1~n中除k外的所有数
        result = [str(k)]  # 先把k放入结果列表
        for i in range(1, n + 1):
            if i != k:
                result.append(str(i))
        # 用空格连接所有元素并输出
        print(*result) #解包
except EOFError:
    exit()