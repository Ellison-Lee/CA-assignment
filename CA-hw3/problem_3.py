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


# Read first line safely
try:
    first_line = input().strip()
    while not first_line:  # Skip empty lines
        first_line = input().strip()
    N = int(first_line)
except EOFError:
    exit()

# Read array
try:
    arr_line = input().strip()
    while not arr_line:  # Skip empty lines
        arr_line = input().strip()
    A = list(map(int, arr_line.split()))
except EOFError:
    A = []

# Read M
try:
    m_line = input().strip()
    while not m_line:  # Skip empty lines
        m_line = input().strip()
    M = int(m_line)
except EOFError:
    M = 0

# Build segment tree
st = SegmentTree(A)

# Process M queries
for _ in range(M):
    try:
        query_line = input().strip()
        while not query_line:  # Skip empty lines
            query_line = input().strip()
        x, y = map(int, query_line.split())
        result = st.query_range(x, y)
        print(result)
    except EOFError:
        break

