""" 
问题：Range Query（区间查询）
给定一个初始数组，支持两种操作：
1. 区间更新：将区间 [l, r] 中的所有元素加上 x
2. 区间求和查询：查询区间 [l, r] 中所有元素的和

算法：使用树状数组维护两个差分数组d[i],i*d[i]

输入格式：
第一行：两个整数 n 和 q，用空格分隔（n为数组长度，q为操作数量）
第二行：n 个整数，用空格分隔，表示初始数组
接下来q行：每行表示一个操作
  - 操作类型1：四个整数 1 l r x，表示将区间 [l, r] 中的所有元素加上 x
  - 操作类型2：三个整数 2 l r，表示查询区间 [l, r] 中所有元素的和

输出格式：
对于每个操作类型2，输出查询结果

示例：
输入：
5 10
2 6 6 1 1
2 1 4
1 2 5 10
2 1 3
2 2 3
1 2 2 8
1 2 3 7
1 4 4 10
2 1 2
1 4 5 6
2 3 4
输出：
15
34
32
33
50
"""
class fenwickTree:
    def __init__(self,size):
        self.n = size
        self.tree = [0]*(size+1) #树状数组储存的是差分数组，因此有效位置是1->size+1，第0位默认为0

    def update(self,idx,delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx #按照树状数组性质，向上层传递delta

    def query(self,idx):
        ans = 0
        while idx > 0:
            ans += self.tree[idx]
            idx -= idx & -idx #按照树状数组性质，向下层求和
        return ans

try: 
    n,q = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # 预处理原数组的前缀和
    prefix = [0]*(n+1)
    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + arr[i-1]
    
    # 方案1：两个树状数组优化（推荐）
    # tree1维护差分数组d[i]，tree2维护i*d[i]
    tree1 = fenwickTree(n)  # 维护 d[i]
    tree2 = fenwickTree(n)  # 维护 i*d[i]

    for _ in range(q):
        info = list(map(int,input().split()))
        if info[0] == 1:
            l,r,x = info[1:]
            # 区间更新 [l, r] + x
            tree1.update(l, x)
            tree1.update(r+1, -x)
            tree2.update(l, l*x)
            tree2.update(r+1, -(r+1)*x)

        elif info[0] == 2:
            l,r = info[1:]
            # 区间查询公式：(r+1)*query1(r) - l*query1(l-1) - (query2(r) - query2(l-1))
            # 时间复杂度：O(log n)
            initial_sum = prefix[r] - prefix[l-1]  # 使用前缀和优化
            diff_sum = (r+1)*tree1.query(r) - l*tree1.query(l-1) - (tree2.query(r) - tree2.query(l-1))
            print(initial_sum + diff_sum)
except EOFError:
    exit()

