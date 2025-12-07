"""
问题：Range Maximum Subarray（区间最大子段和）
给定一个数组，支持多次查询：对于每个查询区间 [x, y]，求该区间内的最大子段和。
最大子段和定义：区间内所有连续子数组的和的最大值。

算法：线段树（Segment Tree）
- 使用线段树维护区间的最大子段和信息
- 每个节点维护四个信息：
  - total_sum: 区间总和
  - max_prefix_sum: 最大前缀和
  - max_suffix_sum: 最大后缀和
  - max_subarray_sum: 最大子段和
- 合并两个子区间时，最大子段和可能出现在：
  1. 左子区间的最大子段和
  2. 右子区间的最大子段和
  3. 左子区间的最大后缀和 + 右子区间的最大前缀和

时间复杂度: 
- 建树：O(n)
- 查询：O(log n)
空间复杂度: O(n)

输入格式：
第一行：一个整数 N，表示数组长度
第二行：N 个整数，用空格分隔，表示数组元素
第三行：一个整数 M，表示查询数量
接下来M行：每行两个整数 x y，用空格分隔，表示查询区间 [x, y]（1-indexed）

输出格式：
对于每个查询，输出区间 [x, y] 的最大子段和

示例：
输入：
3
-1 2 3
1
1 2
输出：
2
"""

class SegmentTreeNode:
    """线段树节点：维护区间最大子段和信息"""
    def __init__(self):
        self.total_sum = 0          # 区间总和
        self.max_prefix_sum = 0     # 最大前缀和
        self.max_suffix_sum = 0     # 最大后缀和
        self.max_subarray_sum = 0   # 最大子段和
    
    def set_value(self, val):
        """设置叶子节点的值"""
        self.total_sum = val
        self.max_prefix_sum = val
        self.max_suffix_sum = val
        self.max_subarray_sum = val


class SegmentTree:
    """线段树：支持区间最大子段和查询"""
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [SegmentTreeNode() for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)
    
    def build(self, node, l, r):
        """构建线段树"""
        if l == r:
            # 叶子节点
            self.tree[node].set_value(self.arr[l])
            return
        
        mid = (l + r) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)
        self.push_up(node, 2 * node, 2 * node + 1)
    
    def push_up(self, parent, left, right):
        """合并左右子节点的信息"""
        # 区间总和
        self.tree[parent].total_sum = self.tree[left].total_sum + self.tree[right].total_sum
        
        # 最大前缀和：左子区间的最大前缀和，或左子区间总和 + 右子区间的最大前缀和
        self.tree[parent].max_prefix_sum = max(
            self.tree[left].max_prefix_sum,
            self.tree[left].total_sum + self.tree[right].max_prefix_sum
        )
        
        # 最大后缀和：右子区间的最大后缀和，或右子区间总和 + 左子区间的最大后缀和
        self.tree[parent].max_suffix_sum = max(
            self.tree[right].max_suffix_sum,
            self.tree[right].total_sum + self.tree[left].max_suffix_sum
        )
        
        # 最大子段和：左子区间、右子区间、或跨越两个子区间
        self.tree[parent].max_subarray_sum = max(
            self.tree[left].max_subarray_sum,
            self.tree[right].max_subarray_sum,
            self.tree[left].max_suffix_sum + self.tree[right].max_prefix_sum
        )
    
    def query(self, node, l, r, ql, qr):
        """查询区间 [ql, qr] 的最大子段和信息"""
        if ql <= l and r <= qr:
            # 完全包含，直接返回
            return self.tree[node]
        
        mid = (l + r) // 2
        
        if qr <= mid:
            # 完全在左子树
            return self.query(2 * node, l, mid, ql, qr)
        elif ql > mid:
            # 完全在右子树
            return self.query(2 * node + 1, mid + 1, r, ql, qr)
        else:
            # 跨越左右子树，需要合并
            left_res = self.query(2 * node, l, mid, ql, mid)
            right_res = self.query(2 * node + 1, mid + 1, r, mid + 1, qr)
            
            # 合并结果
            result = SegmentTreeNode()
            result.total_sum = left_res.total_sum + right_res.total_sum
            result.max_prefix_sum = max(
                left_res.max_prefix_sum,
                left_res.total_sum + right_res.max_prefix_sum
            )
            result.max_suffix_sum = max(
                right_res.max_suffix_sum,
                right_res.total_sum + left_res.max_suffix_sum
            )
            result.max_subarray_sum = max(
                left_res.max_subarray_sum,
                right_res.max_subarray_sum,
                left_res.max_suffix_sum + right_res.max_prefix_sum
            )
            return result
    
    def query_range(self, ql, qr):
        """查询区间 [ql, qr] 的最大子段和（1-indexed）"""
        # 转换为 0-indexed
        res = self.query(1, 0, self.n - 1, ql - 1, qr - 1)
        return res.max_subarray_sum


# 读取输入
try:
    # 读取第一行
    first_line = input().strip()
    while not first_line:  # 跳过空行
        first_line = input().strip()
    N = int(first_line)
    
    # 读取数组
    arr_line = input().strip()
    while not arr_line:  # 跳过空行
        arr_line = input().strip()
    A = list(map(int, arr_line.split()))
    
    # 读取M
    m_line = input().strip()
    while not m_line:  # 跳过空行
        m_line = input().strip()
    M = int(m_line)
    
    # 构建线段树
    st = SegmentTree(A)
    
    # 处理M个查询
    for _ in range(M):
        query_line = input().strip()
        while not query_line:  # 跳过空行
            query_line = input().strip()
        x, y = map(int, query_line.split())
        result = st.query_range(x, y)
        print(result)
except EOFError:
    exit(0)

