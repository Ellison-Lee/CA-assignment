class FenwickTree:
    """树状数组（Fenwick Tree）：用于维护差分数组的前缀和"""
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        """在位置 index 加上 delta"""
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        """查询前缀和 [1, index]"""
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


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

# Initialize Fenwick Tree for difference array
# 使用树状数组维护差分数组，实现 O(log n) 的区间更新和点查询
ft = FenwickTree(n)

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
        # 区间更新：在差分数组中，l 位置 +x，r+1 位置 -x
        l, r, x = op_data[1], op_data[2], op_data[3]
        ft.update(l, x)
        if r + 1 <= n:
            ft.update(r + 1, -x)
    else:
        # Type 2: Point query a[i]
        # 点查询：初始值 + 差分数组的前缀和
        i = op_data[1]
        result = initial_arr[i - 1] + ft.query(i)
        print(result)

