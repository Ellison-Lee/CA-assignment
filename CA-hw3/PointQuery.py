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
    tree = fenwickTree(n)

    for _ in range(q):
        info = list(map(int,input().split()))
        if info[0] == 1: #区间加数
            l,r,x = info[1:]
            tree.update(l,x) #[l,r]位置+x，即在l处差分数组+x
            tree.update(r+1,-x) #在r+1处差分数组-x

        elif info[0] == 2: #查询元素
            i = info[1]
            print(arr[i-1]+tree.query(i))
except EOFError:
    exit()

