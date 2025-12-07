"""
问题: K Co-prime Permutation
构造一个排列，使得恰好有k个位置i满足gcd(p_i, i) = 1

核心思路：
关键洞察：交换位置i和j（即perm[i]=j, perm[j]=i）的效果：
- 如果gcd(i,j)=1，则两个位置都互质，贡献2个
- 如果gcd(i,j)>1，则两个位置都不互质，贡献0个

最简单的构造策略：
1. 初始化为单位排列perm[i]=i
2. 将前n-k个位置两两交换：1↔2, 3↔4, 5↔6, ...
   - 但要注意选择合适的交换方式
3. 将后k个位置两两交换或反转

时间复杂度: O(n)
空间复杂度: O(n)
输入：
5 3
输出：
1 4 5 2 3

"""

import math


def gcd(a, b):
    """计算最大公约数"""
    while b:
        a, b = b, a % b
    return a


def solve(n, k):
    """
    构造k互质排列
    
    最标准的构造方法：
    - 将数组分成两半交换，然后根据k调整
    - 或者直接：前(n-k)个顺序，后k个逆序
    
    经典构造：
    - perm = [1, 2, ..., n-k, n, n-1, ..., n-k+1]
    - 前(n-k)个位置i：perm[i] = i，只有i=1时互质
    - 后k个位置：反转后容易互质
    
    但这个方法前(n-k)个只有1个互质（位置1），后k个不一定全互质
    
    改进：将整个数组分两半完全交换
    
    :param n: 排列长度
    :param k: 需要的互质位置数
    :return: 排列列表，或-1表示无解
    """
    # 必要条件：n和k的奇偶性必须相同
    if (n - k) % 2 != 0:
        return -1
    
    # 使用经典构造方法：
    # 将数组[1..n]分成两半：[1..n/2]和[n/2+1..n]
    # 完全交换：perm = [n/2+1, ..., n, 1, ..., n/2]
    mid = n // 2
    perm = list(range(mid + 1, n + 1)) + list(range(1, mid + 1))
    
    # 调整：如果需要减少互质数，将前(n-k)/2对恢复原位
    # 恢复意味着让perm[i] = i
    for i in range((n - k) // 2):
        # 将位置i+1恢复为i+1
        # 但要同时处理被交换的另一半
        perm[i] = i + 1
        perm[mid + i] = mid + i + 1
    
    return perm


def verify(perm, k):
    """验证排列是否满足条件（仅用于调试）"""
    n = len(perm)
    count = 0
    for i in range(1, n + 1):
        if gcd(perm[i - 1], i) == 1:
            count += 1
    return count == k


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取输入
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        n, k = map(int, first_line.split())
        
        # 求解
        result = solve(n, k)
        
        # 输出结果
        if result == -1:
            print(-1)
        else:
            print(' '.join(map(str, result)))
            
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

