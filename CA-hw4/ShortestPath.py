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
from collections import defaultdict
import heapq


def dijkstra(n,graph,start,end):
    dist = [float("inf")] *(n+1) #dsit[i]是i节点到start节点的距离
    dist[start] = 0 #自身距离是0
    visited = [] #储存访问过的节点
    hq = [[0,start]] #最小堆保存各个点到start的最小距离

    while hq:
        curr_dist,u = heapq.heappop(hq)

        if u in visited:#如果访问过就跳过
            continue
        else:
            visited.append(u)
        if u == end: #如果找到了end就返回最小距离
            return curr_dist
        if curr_dist > dist[u]: #如果当前最小距离比dist还大就跳过
            continue

        for v,w in graph[u]: #遍历u的邻居，查看邻居v经过u到start是否更近
            new_dist = curr_dist+w
            if new_dist < dist[v]: #如果更近就加入最小堆
                dist[v] = new_dist
                heapq.heappush(hq,[new_dist,v])
    return dist[end]
1
try:
    n,m,s,t = list(map(int,input().split()))
    graph = defaultdict(list)
    for _ in range(m):
        u,v,w = list(map(int,input().split()))
        graph[u].append([v,w])
        graph[v].append([u,w])

    print(dijkstra(n,graph,s,t))
except EOFError:
    exit()