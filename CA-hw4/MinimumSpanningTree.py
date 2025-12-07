"""
问题1: 最小生成树 (Minimum Spanning Tree)
使用Kruskal算法 + 并查集优化
时间复杂度: O(E log E) 其中E是边数
空间复杂度: O(V + E) 其中V是顶点数
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
    """并查集数据结构，用于高效地检测环和合并集合"""
    
    def __init__(self, n):
        """
        初始化并查集
        :param n: 元素数量
        """
        self.parent = list(range(n + 1))  # parent[i] 表示节点i的父节点
        self.rank = [0] * (n + 1)  # rank[i] 表示以i为根的树的秩（高度）
    
    def find(self, x):
        """
        查找元素x所在集合的根节点（带路径压缩优化）
        :param x: 要查找的元素
        :return: x所在集合的根节点
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]
    
    def union(self, x, y):
        """
        合并x和y所在的两个集合（按秩合并优化）
        :param x: 第一个元素
        :param y: 第二个元素
        :return: 如果成功合并返回True，如果已在同一集合返回False
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # 已经在同一集合中，合并会形成环
        
        # 按秩合并：将秩较小的树连接到秩较大的树下
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True


def kruskal_mst(n, edges):
    """
    使用Kruskal算法计算最小生成树的权重和
    
    算法步骤：
    1. 将所有边按权重从小到大排序
    2. 初始化并查集
    3. 依次考虑每条边：
       - 如果边的两个端点不在同一连通分量中，则选择这条边
       - 否则跳过这条边（选择会形成环）
    4. 重复步骤3直到选择了n-1条边
    
    :param n: 顶点数量
    :param edges: 边的列表，每条边是(u, v, w)的形式
    :return: 最小生成树的总权重
    """
    # 步骤1: 按权重排序，时间复杂度 O(E log E)
    edges.sort(key=lambda x: x[2])
    
    # 步骤2: 初始化并查集
    uf = UnionFind(n)
    
    # 步骤3: 贪心选择边
    mst_weight = 0  # 最小生成树的总权重
    edges_count = 0  # 已选择的边数
    
    for u, v, w in edges:
        # 如果u和v不在同一连通分量中
        if uf.union(u, v):
            mst_weight += w
            edges_count += 1
            
            # 最小生成树包含n-1条边
            if edges_count == n - 1:
                break
    
    return mst_weight


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取第一行：顶点数n和边数m
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        n, m = map(int, first_line.split())
        
        # 读取m条边
        edges = []
        for _ in range(m):
            line = input().strip()
            while not line:  # 跳过空行
                line = input().strip()
            u, v, w = map(int, line.split())
            edges.append((u, v, w))
        
        # 计算最小生成树的总权重
        result = kruskal_mst(n, edges)
        
        # 输出结果
        print(result)
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

