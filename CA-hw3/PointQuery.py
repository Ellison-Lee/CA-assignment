"""
问题：Range Update/Point Query（区间更新/点查询）
给定一个初始数组，支持两种操作：
1. 区间更新：将区间 [l, r] 中的所有元素加上 x
2. 点查询：查询位置 i 的元素值

算法：树状数组维护差分数组
- 使用差分数组的思想：对于区间更新 [l, r] + x，在差分数组中只需更新两个位置来保存更新的历史信息
  - diff[l] += x
  - diff[r+1] -= x
- 使用树状数组维护差分数组的前缀和，实现高效的区间更新和点查询
- 查询位置 i 的值 = 初始值[i] + 差分数组的前缀和[1..i]

时间复杂度: 
- 区间更新：O(log n)
- 点查询：O(log n)


输入格式：
第一行：两个整数 n 和 q，用空格分隔（n为数组长度，q为操作数量）
第二行：n 个整数，用空格分隔，表示初始数组
接下来q行：每行表示一个操作
  - 操作类型1：四个整数 1 l r x，表示将区间 [l, r] 中的所有元素加上 x
  - 操作类型2：两个整数 2 i，表示查询位置 i 的元素值

输出格式：
对于每个操作类型2，输出查询结果

示例：
输入：
3 2
1 2 3
1 1 3 1
2 2
输出：
2
"""

class FenwickTree:
    """树状数组：用于维护差分数组的前缀和"""
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        """在位置 index 加上 delta"""
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        """查询前缀和 [1, index]"""
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


# 读取输入
try:
    # 读取第一行
    first_line = input().strip()
    n, q = map(int, first_line.split())
    
    # 读取初始数组
    arr_line = input().strip()
    initial_arr = list(map(int, arr_line.split()))
    
    # 初始化树状数组维护差分数组，实现 O(log n) 的区间更新和点查询
    ft = FenwickTree(n)
    
    # 处理q个操作
    for _ in range(q):
        op_line = input().strip()
        op_data = list(map(int, op_line.split()))
        
        if op_data[0] == 1:
            # Type 1: Range update [l, r] add x
            # 区间更新：在差分数组中，l 位置 +x，r+1 位置 -x
            l, r, x = op_data[1], op_data[2], op_data[3]
            ft.update(l, x)
            if r + 1 <= n:
                ft.update(r + 1, -x)
        else:
            # Type 2: Point query a[i]
            # 点查询：初始值 + 差分数组的前缀和
            i = op_data[1]
            result = initial_arr[i - 1] + ft.query(i)
            print(result)
except EOFError:
    exit(0)


