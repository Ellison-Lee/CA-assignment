"""
问题3: 最低公共祖先 (Lowest Common Ancestor, LCA)
使用倍增算法（Binary Lifting）
预处理时间复杂度: O(N log N)
查询时间复杂度: O(log N)
空间复杂度: O(N log N)
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
    """使用倍增算法实现的最低公共祖先查询"""
    
    def __init__(self, n, root):
        """
        初始化 LCA 数据结构
        :param n: 节点数量
        :param root: 根节点编号
        """
        self.n = n
        self.root = root
        self.graph = defaultdict(list)  # 邻接表
        
        # 计算需要的最大跳跃层数 (log2(n) 向上取整)
        self.max_log = math.ceil(math.log2(n)) + 1 if n > 1 else 1
        
        # up[u][i] 表示从节点 u 向上走 2^i 步到达的祖先
        # 如果不存在则为 -1
        self.up = [[-1] * self.max_log for _ in range(n + 1)]
        
        # depth[u] 表示节点 u 的深度（根节点深度为 0）
        self.depth = [0] * (n + 1)
    
    def add_edge(self, u, v):
        """
        添加一条边（无向边）
        :param u: 节点 u
        :param v: 节点 v
        """
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def preprocess(self):
        """
        预处理：构建倍增表和深度信息
        使用迭代DFS遍历树，计算每个节点的父节点和深度
        """
        # 使用迭代DFS遍历树，初始化深度和直接父节点
        # 栈中存储 (当前节点, 父节点, 深度)
        stack = [(self.root, -1, 0)]
        
        while stack:
            u, parent, d = stack.pop()
            self.depth[u] = d
            self.up[u][0] = parent  # 向上走 2^0 = 1 步到达的节点就是父节点
            
            for v in self.graph[u]:
                if v != parent:  # 避免回到父节点
                    stack.append((v, u, d + 1))
        
        # 构建倍增表
        # up[u][i] = up[up[u][i-1]][i-1]
        # 即：从 u 向上走 2^i 步 = 先走 2^(i-1) 步，再走 2^(i-1) 步
        for i in range(1, self.max_log):
            for u in range(1, self.n + 1):
                if self.up[u][i - 1] != -1:
                    self.up[u][i] = self.up[self.up[u][i - 1]][i - 1]
    
    def query(self, a, b):
        """
        查询节点 a 和 b 的最低公共祖先
        
        算法步骤：
        1. 确保 a 的深度 >= b 的深度（如果不是则交换）
        2. 将 a 提升到与 b 相同的深度
        3. 如果此时 a == b，则 a 就是 LCA
        4. 否则，同时将 a 和 b 向上移动，直到它们的父节点相同
        
        :param a: 节点 a
        :param b: 节点 b
        :return: a 和 b 的最低公共祖先
        """
        # 确保 a 的深度 >= b 的深度
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        
        # 将 a 提升到与 b 相同的深度
        diff = self.depth[a] - self.depth[b]
        for i in range(self.max_log):
            if (diff >> i) & 1:  # 如果 diff 的第 i 位是 1
                if self.up[a][i] != -1:  # 检查是否存在这个祖先
                    a = self.up[a][i]
        
        # 如果此时 a == b，说明 b 是 a 的祖先
        if a == b:
            return a
        
        # 同时将 a 和 b 向上移动
        # 从大到小尝试每个跳跃大小，确保不会跳过 LCA
        for i in range(self.max_log - 1, -1, -1):
            if self.up[a][i] != -1 and self.up[b][i] != -1 and self.up[a][i] != self.up[b][i]:
                a = self.up[a][i]
                b = self.up[b][i]
        
        # 此时 a 和 b 的父节点就是 LCA
        return self.up[a][0]


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取第一行：节点数 N、查询数 M、根节点 S
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        n, m, s = map(int, first_line.split())
        
        # 创建 LCA 对象
        lca = LCA(n, s)
        
        # 读取 N-1 条边（树有 N-1 条边）
        for _ in range(n - 1):
            line = input().strip()
            while not line:  # 跳过空行
                line = input().strip()
            x, y = map(int, line.split())
            lca.add_edge(x, y)
        
        # 预处理
        lca.preprocess()
        
        # 处理 M 个查询
        for _ in range(m):
            line = input().strip()
            while not line:  # 跳过空行
                line = input().strip()
            a, b = map(int, line.split())
            
            # 查询并输出结果
            result = lca.query(a, b)
            print(result)
            
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

