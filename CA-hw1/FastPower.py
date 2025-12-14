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
mod = 998244353
#读数据

info=input()
x,k=map(int,info.split())


x = x%mod
ans=1
while k >=1:
    if k%2 == 1:
        ans = ans*x%mod #奇数乘自己

    x = x*x%mod #偶数翻番
    k = k//2

print(ans)

