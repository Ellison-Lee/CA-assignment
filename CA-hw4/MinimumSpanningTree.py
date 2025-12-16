"""
最小生成树 (Minimum Spanning Tree)
使用Kruskal算法 + 并查集优化
时间复杂度: O(E log E) 其中E是边数
输入：
7 12
1 2 9
1 5 2
1 6 3
2 3 5
2 6 7
3 4 6
3 7 3
4 5 6
4 7 2
5 6 3
5 7 6
6 7 1
输出：
16
"""
class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n+1)) #初始化父节点，即元素本身
        self.rank = [1]*(n+1)

    def find(self,a): #查询当前a所在集合的根节点
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self,a,b): #合并a,b所在集合
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b: #a,b在同一个集合
            return False
        #小树加入大树
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] +=1
        return True

def kruskal(n,edges): #每次合并最小边
    A = UnionFind(n)
    edges.sort(key=lambda x:x[2])
    weights = 0
    count = 0
    for u,v,w in edges:
        if A.union(u,v):
            weights += w
            count += 1
    return weights

try:
    n,m = list(map(int,input().split()))
    edges=[]
    for _ in range(m):
        edge = list(map(int,input().split()))
        edges.append((edge))
    print(kruskal(n,edges))
except EOFError:
    exit()
