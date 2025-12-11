"""
问题2: 最短路径 (Shortest Path)
使用Dijkstra算法 + 优先队列优化
时间复杂度: O((V + E) log V) 其中V是顶点数，E是边数
空间复杂度: O(V + E)
输入：
7 11 5 4
2 4 2
1 4 3
7 2 2
3 4 3
5 7 5
7 3 3
6 1 1
6 3 4
2 4 3
5 6 3
7 2 1
输出：
7
"""

import heapq
from collections import defaultdict


def dijkstra(n, graph, start, end):
    """
    使用Dijkstra算法计算从start到end的最短路径
    
    算法原理：
    Dijkstra算法是一种贪心算法，用于计算单源最短路径。
    它维护一个距离数组，逐步确定每个顶点到起点的最短距离。
    
    算法步骤：
    1. 初始化：将起点距离设为0，其他顶点距离设为无穷大
    2. 使用优先队列（最小堆）存储待处理的顶点
    3. 每次从队列中取出距离最小的顶点u
    4. 对于u的每个邻居v，如果通过u到达v的距离更短，则更新v的距离
    5. 重复步骤3-4直到处理完所有可达顶点或找到目标顶点
    
    :param n: 顶点数量
    :param graph: 邻接表表示的图，graph[u] = [(v, w), ...]表示u到v有权重为w的边
    :param start: 起始顶点
    :param end: 目标顶点
    :return: 从start到end的最短路径长度
    """
    # 初始化距离数组，所有距离初始化为无穷大
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    
    # 优先队列：存储(距离, 顶点)对
    # Python的heapq是最小堆，会自动按距离排序
    pq = [(0, start)]  # (distance, vertex)
    
    # 记录已经确定最短路径的顶点
    visited = set()
    
    while pq:
        # 取出当前距离最小的顶点
        curr_dist, u = heapq.heappop(pq)
        
        # 如果已经处理过这个顶点，跳过
        if u in visited:
            continue
        
        # 标记为已访问
        visited.add(u)
        
        # 如果到达目标顶点，直接返回
        if u == end:
            return curr_dist
        
        # 如果当前距离大于已记录的最短距离，跳过
        # （这种情况发生在同一顶点被多次加入队列时）
        if curr_dist > dist[u]:
            continue
        
        # 松弛操作：更新所有邻居的距离
        for v, w in graph[u]:
            new_dist = dist[u] + w
            
            # 如果找到更短的路径，更新距离并加入队列
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    # 返回到目标顶点的最短距离
    return dist[end]


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取第一行：顶点数n、边数m、起点s、终点t
        first_line = input().strip()
        n, m, s, t = map(int, first_line.split())
        
        # 构建邻接表
        # graph[u] 存储从u出发的所有边：[(v, w), ...]
        graph = defaultdict(list)
        
        # 读取m条边
        for _ in range(m):
            line = input().strip()
            u, v, w = map(int, line.split())
            
            # 无向图：添加双向边
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # 计算最短路径
        result = dijkstra(n, graph, s, t)
        
        # 输出结果
        print(result)
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

