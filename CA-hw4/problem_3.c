/*
问题3: 最低公共祖先 (Lowest Common Ancestor, LCA)
使用倍增算法（Binary Lifting）- C语言实现
预处理时间复杂度: O(N log N)
查询时间复杂度: O(log N)
空间复杂度: O(N log N)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 500005  // 最大节点数
#define MAXLOG 20    // log2(500000) ≈ 19

// 邻接表结构
typedef struct Edge {
    int to;
    struct Edge* next;
} Edge;

// 全局变量
Edge* graph[MAXN];      // 邻接表
int up[MAXN][MAXLOG];   // up[u][i] 表示从节点u向上走2^i步到达的祖先
int depth[MAXN];        // depth[u] 表示节点u的深度
int n, m, s;            // 节点数、查询数、根节点
int max_log;            // 最大跳跃层数

// 添加边到邻接表
void add_edge(int u, int v) {
    Edge* e = (Edge*)malloc(sizeof(Edge));
    e->to = v;
    e->next = graph[u];
    graph[u] = e;
}

// 递归DFS遍历树，初始化深度和直接父节点
void dfs(int u, int parent, int d) {
    depth[u] = d;
    up[u][0] = parent;  // 向上走2^0=1步到达的节点就是父节点
    
    // 遍历所有相邻节点
    for (Edge* e = graph[u]; e != NULL; e = e->next) {
        int v = e->to;
        if (v != parent) {  // 避免回到父节点
            dfs(v, u, d + 1);
        }
    }
}

// 预处理：构建倍增表
void preprocess() {
    // 初始化up数组为-1
    memset(up, -1, sizeof(up));
    memset(depth, 0, sizeof(depth));
    
    // DFS遍历树，初始化深度和直接父节点
    dfs(s, -1, 0);
    
    // 构建倍增表
    // up[u][i] = up[up[u][i-1]][i-1]
    for (int i = 1; i < max_log; i++) {
        for (int u = 1; u <= n; u++) {
            if (up[u][i - 1] != -1) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }
        }
    }
}

// 查询节点a和b的最低公共祖先
int query(int a, int b) {
    // 确保a的深度 >= b的深度
    if (depth[a] < depth[b]) {
        int temp = a;
        a = b;
        b = temp;
    }
    
    // 将a提升到与b相同的深度
    int diff = depth[a] - depth[b];
    for (int i = 0; i < max_log; i++) {
        if ((diff >> i) & 1) {  // 如果diff的第i位是1
            if (up[a][i] != -1) {
                a = up[a][i];
            }
        }
    }
    
    // 如果此时a == b，说明b是a的祖先
    if (a == b) {
        return a;
    }
    
    // 同时将a和b向上移动
    // 从大到小尝试每个跳跃大小，确保不会跳过LCA
    for (int i = max_log - 1; i >= 0; i--) {
        if (up[a][i] != -1 && up[b][i] != -1 && up[a][i] != up[b][i]) {
            a = up[a][i];
            b = up[b][i];
        }
    }
    
    // 此时a和b的父节点就是LCA
    return up[a][0];
}

int main() {
    // 读取第一行：节点数N、查询数M、根节点S
    scanf("%d %d %d", &n, &m, &s);
    
    // 计算最大跳跃层数
    max_log = (int)ceil(log2(n)) + 1;
    if (max_log > MAXLOG) {
        max_log = MAXLOG;
    }
    
    // 初始化邻接表
    memset(graph, 0, sizeof(graph));
    
    // 读取N-1条边（树有N-1条边）
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        add_edge(x, y);
        add_edge(y, x);
    }
    
    // 预处理
    preprocess();
    
    // 处理M个查询
    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        
        // 查询并输出结果
        int result = query(a, b);
        printf("%d\n", result);
    }
    
    return 0;
}

