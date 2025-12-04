class SegmentTreeNode:
    """线段树节点：维护区间总和和懒惰标记"""
    def __init__(self):
        self.total_sum = 0          # 区间总和
        self.lazy_tag = 0           # 懒惰标记，表示需要加到区间内的值


class SegmentTree:
    """线段树：支持区间更新和区间求和查询（带懒标记）"""
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [SegmentTreeNode() for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)
    
    def build(self, node, start, end):
        """构建线段树"""
        if start == end:
            # 叶子节点
            self.tree[node].total_sum = self.arr[start]
            return
        
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        # 更新父节点的总和
        self.tree[node].total_sum = self.tree[2 * node].total_sum + self.tree[2 * node + 1].total_sum
    
    def push_down(self, node, start, end):
        """将当前节点的懒惰标记下推给子节点"""
        if self.tree[node].lazy_tag != 0:
            mid = (start + end) // 2
            left_len = mid - start + 1
            right_len = end - mid
            
            # 更新左子节点
            self.tree[2 * node].total_sum += self.tree[node].lazy_tag * left_len
            self.tree[2 * node].lazy_tag += self.tree[node].lazy_tag
            
            # 更新右子节点
            self.tree[2 * node + 1].total_sum += self.tree[node].lazy_tag * right_len
            self.tree[2 * node + 1].lazy_tag += self.tree[node].lazy_tag
            
            # 清除当前节点的懒惰标记
            self.tree[node].lazy_tag = 0
    
    def update_range(self, node, start, end, ql, qr, val):
        """区间更新：将 [ql, qr] 范围内的元素加上 val（0-indexed）"""
        if qr < start or end < ql:
            # 当前区间与更新区间无交集
            return
        
        if ql <= start and end <= qr:
            # 当前区间完全包含在更新区间内
            self.tree[node].total_sum += val * (end - start + 1)
            self.tree[node].lazy_tag += val
            return
        
        # 下推懒惰标记
        self.push_down(node, start, end)
        
        mid = (start + end) // 2
        self.update_range(2 * node, start, mid, ql, qr, val)
        self.update_range(2 * node + 1, mid + 1, end, ql, qr, val)
        
        # 更新当前节点的总和
        self.tree[node].total_sum = self.tree[2 * node].total_sum + self.tree[2 * node + 1].total_sum
    
    def query_range_sum(self, node, start, end, ql, qr):
        """区间求和查询：查询 [ql, qr] 范围内的元素总和（0-indexed）"""
        if qr < start or end < ql:
            # 当前区间与查询区间无交集
            return 0
        
        if ql <= start and end <= qr:
            # 当前区间完全包含在查询区间内
            return self.tree[node].total_sum
        
        # 下推懒惰标记
        self.push_down(node, start, end)
        
        mid = (start + end) // 2
        left_sum = self.query_range_sum(2 * node, start, mid, ql, qr)
        right_sum = self.query_range_sum(2 * node + 1, mid + 1, end, ql, qr)
        return left_sum + right_sum
    
    def update(self, l, r, val):
        """区间更新接口（1-indexed）"""
        self.update_range(1, 0, self.n - 1, l - 1, r - 1, val)
    
    def query(self, l, r):
        """区间求和查询接口（1-indexed）"""
        return self.query_range_sum(1, 0, self.n - 1, l - 1, r - 1)


# Read first line safely
try:
    first_line = input().strip()
    while not first_line:  # Skip empty lines
        first_line = input().strip()
    n, q = map(int, first_line.split())
except EOFError:
    exit()

# Read initial array
try:
    arr_line = input().strip()
    while not arr_line:  # Skip empty lines
        arr_line = input().strip()
    initial_arr = list(map(int, arr_line.split()))
except EOFError:
    initial_arr = []

# Initialize segment tree
st = SegmentTree(initial_arr)

# Process q operations
for _ in range(q):
    try:
        op_line = input().strip()
        while not op_line:  # Skip empty lines
            op_line = input().strip()
        op_data = list(map(int, op_line.split()))
    except EOFError:
        break
    
    if op_data[0] == 1:
        # Type 1: Range update [l, r] add x
        l, r, x = op_data[1], op_data[2], op_data[3]
        st.update(l, r, x)
    else:
        # Type 2: Range sum query [l, r]
        l, r = op_data[1], op_data[2]
        result = st.query(l, r)
        print(result)

