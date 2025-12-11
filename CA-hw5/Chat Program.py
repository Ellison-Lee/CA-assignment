"""
Chat Program - 最大化第k大元素

问题描述：
给定一个整数序列，可以选择一个连续子数组，将等差数列加到该子数组上。
目标是最大化操作后序列中第k大的元素。

算法思路：
1. 枚举所有可能的子数组起始位置（包括不执行操作）
2. 对每个位置，执行操作并计算第k大元素
3. 返回所有可能结果中的最大值

时间复杂度：O(n² log n)
- 枚举n个起始位置：O(n)
- 每次需要复制数组并排序：O(n log n)
- 总体：O(n² log n)

空间复杂度：O(n)

输入：
6 4 3 1 2
1 1 4 5 1 4
输出：
4
"""

def find_kth_largest(arr, k):
    """
    找到数组中第k大的元素
    
    Args:
        arr: 整数数组
        k: 要找的第k大（k从1开始）
    
    Returns:
        第k大的元素值
    """
    # 降序排序，第k大就是索引k-1的元素
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[k - 1]


def solve(n, k, m, c, d, a):
    """
    解决Chat Program问题
    
    Args:
        n: 序列长度
        k: 要最大化的第k大元素
        m: 子数组长度
        c: 等差数列首项
        d: 等差数列公差
        a: 原始序列
    
    Returns:
        操作后第k大元素的最大可能值
    """
    # 预计算等差数列
    arithmetic_seq = [c + d * i for i in range(m)]
    
    # 初始化结果为不执行操作时的第k大元素
    max_kth_largest = find_kth_largest(a, k)
    
    # 枚举所有可能的起始位置p（从0开始索引）
    for p in range(n - m + 1):
        # 创建临时数组并执行操作
        temp_arr = a[:]
        for i in range(m):
            temp_arr[p + i] += arithmetic_seq[i]
        
        # 计算操作后的第k大元素
        kth_largest = find_kth_largest(temp_arr, k)
        
        # 更新最大值
        max_kth_largest = max(max_kth_largest, kth_largest)
    
    return max_kth_largest


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取第一行：n, k, m, c, d
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        n, k, m, c, d = map(int, first_line.split())
        
        # 读取第二行：序列a
        second_line = input().strip()
        while not second_line:  # 跳过空行
            second_line = input().strip()
        a = list(map(int, second_line.split()))
        
        # 求解并输出结果
        result = solve(n, k, m, c, d, a)
        print(result)
    
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

