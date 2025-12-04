"""
问题4: 并查集 (Union-Find / Disjoint Set Union)
使用路径压缩和按秩合并优化
时间复杂度: O(M * α(N))，其中α是阿克曼函数的反函数，几乎为常数
空间复杂度: O(N)
"""

MOD = 998244353


class UnionFind:
    """并查集数据结构，支持合并和查询操作"""
    
    def __init__(self, n):
        """
        初始化并查集
        :param n: 元素数量（0到n-1）
        """
        self.parent = list(range(n))  # parent[i] 表示元素i的父节点
        self.rank = [0] * n           # rank[i] 表示以i为根的树的秩（近似高度）
    
    def find(self, x):
        """
        查找元素x的根节点（代表元），使用路径压缩优化
        :param x: 要查找的元素
        :return: x所在集合的根节点
        """
        if self.parent[x] != x:
            # 路径压缩：将x到根节点路径上的所有节点直接连接到根节点
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        合并包含x和y的两个集合，使用按秩合并优化
        :param x: 第一个元素
        :param y: 第二个元素
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # 如果已经在同一个集合中，无需合并
        if root_x == root_y:
            return
        
        # 按秩合并：将秩小的树连接到秩大的树上
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # 秩相同时，任意选择一个作为根，并增加其秩
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
    
    def is_connected(self, x, y):
        """
        查询x和y是否在同一个集合中
        :param x: 第一个元素
        :param y: 第二个元素
        :return: True如果在同一集合，False否则
        """
        return self.find(x) == self.find(y)


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取第一行：集合数n和操作数m
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        n, m = map(int, first_line.split())
        
        # 创建并查集
        uf = UnionFind(n)
        
        # 存储所有查询操作的结果
        query_results = []
        
        # 处理m个操作
        for _ in range(m):
            line = input().strip()
            while not line:  # 跳过空行
                line = input().strip()
            op, i, j = map(int, line.split())
            
            if op == 0:
                # 合并操作
                uf.union(i, j)
            else:  # op == 1
                # 查询操作
                if uf.is_connected(i, j):
                    query_results.append('1')
                else:
                    query_results.append('0')
        
        # 将查询结果连接成二进制字符串
        binary_string = ''.join(query_results)
        
        # 如果没有查询操作，输出0
        if not binary_string:
            print(0)
            return
        
        # 将二进制字符串转换为整数，并取模
        # 为了避免整数过大，边计算边取模
        result = 0
        for bit in binary_string:
            result = (result * 2 + int(bit)) % MOD
        
        print(result)
        
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

