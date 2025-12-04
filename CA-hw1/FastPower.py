"""
问题1: 快速幂算法 (Fast Exponentiation / Binary Exponentiation)
计算 x^k mod 998244353
时间复杂度: O(log k)

输入格式：
一行，包含两个整数 x 和 k，用空格分隔

输出格式：
输出 x^k mod 998244353 的结果

示例：
输入：
2 10
输出：
1024
"""
MOD = 998244353
def fast_power(x, k, mod):
    """
    使用快速幂算法计算 x^k mod mod
    
    算法原理：
    - 将指数k表示为二进制形式
    - 利用 x^k = x^(b_n*2^n + b_(n-1)*2^(n-1) + ... + b_1*2 + b_0)
    - 每次将x平方，如果当前位为1则乘到结果中
    """
    ans = 1
    x %= mod
    
    while k > 0:
        if k % 2 == 1:  # 如果k是奇数
            ans = ans * x % mod
        x = x * x % mod
        k //= 2
    
    return ans

    #3^3 
def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取输入
        first_line = input()
        while not first_line:  # 跳过空行
            first_line = input()
        x, k = map(int, first_line.split())
        
        # 计算结果
        result = fast_power(x, k, MOD)
        
        # 输出结果
        print(result)
        
    except EOFError:
        exit()
if __name__ == "__main__":
    main()