"""
问题3: 最低公共祖先 (Lowest Common Ancestor, LCA)
使用倍增算法（Binary Lifting）
预处理时间复杂度: O(N log N)
查询时间复杂度: O(log N)
输入：
5 5 4
3 1
2 4
5 1
1 4
2 4
3 2
3 5
1 2
4 5
输出：
4
4
1
4
4
"""
from collections import defaultdict
import math

class LCA:
    def __init__(self,n,root):
        self.n = n
        self.root = root
        self.max_log = math.ceil(math.log2(n))
        self.graph = defaultdict(list) #初始化邻接表
        self.depth = [0]*(n+1) #depth[i]是节点i的深度
        self.up = [[-1]*self.max_log for _ in range(n+1)] #倍增数组up[i][j]表示节点i向上跳2^j层到达的parent

    def add_edge(self,u,v): #按照输入加上边
        self.graph[u].append(v)
        self.graph[v].append(u)

    def prepocess(self): #预处理，DFS初始化depth，up
        stack = [[self.root,-1,0]]
        while stack: #完善深度，父节点
            u,parent,d = stack.pop()
            self.depth[u] = d
            self.up[u][0] = parent

            for v in self.graph[u]:
                if v != parent: #避免是parent
                    stack.append([v,u,d+1])

        for d in range(1,self.max_log): #完善倍增表
            for u in range(1,self.n+1):
                if self.up[u][d-1] != -1:
                    self.up[u][d] = self.up[self.up[u][d-1]][d-1]

    def query(self,a,b):
        if self.depth[a] < self.depth[b]: #保证a的深度比b大
            a,b = b,a
        #把a提升至b的深度
        diff = self.depth[a] - self.depth[b]
        for i in range(self.max_log):
            if (diff >> i) & 1:
                a = self.up[a][i]

        if a == b: #如果提升a后=b，则LCA=b
            return a

        for i in range(self.max_log-1,-1,-1):#同时提升a,b找LCA
            if self.up[a][i]!=-1 and self.up[b][i]!=-1 and self.up[a][i]!=self.up[b][i]:
                a = self.up[a][i]
                b = self.up[b][i]

        return self.up[a][0]

try:
    n,m,s = list(map(int,input().split()))
    A = LCA(n,s)
    for _ in range(n-1):
        a,b = list(map(int,input().split()))
        A.add_edge(a,b)
    A.prepocess()
    for _ in range(m):
        a,b = list(map(int,input().split()))
        print(A.query(a,b))
except EOFError:
    exit()



