class SegmentTree:
    """线段树：维护区间覆盖和实际长度"""
    def __init__(self, coords):
        self.x_coords = coords[:]  # 实际坐标值
        self.n = len(coords) - 1  # 区间数 = 点数 - 1
        self.cover = [0] * (4 * self.n)  # 覆盖次数
        self.len = [0] * (4 * self.n)  # 被覆盖的实际总长度
    
    def get_length(self, l, r):
        """获取区间 [l, r] 的实际长度"""
        return self.x_coords[r + 1] - self.x_coords[l]
    
    def update(self, node, l, r, ql, qr, val):
        """更新线段树节点"""
        if qr < l or ql > r:
            return
        
        if ql <= l and r <= qr:
            self.cover[node] += val
            if self.cover[node] > 0:
                self.len[node] = self.get_length(l, r)
            else:
                if l == r:
                    self.len[node] = 0
                else:
                    self.len[node] = self.len[2*node] + self.len[2*node+1]
            return
        
        mid = (l + r) // 2
        self.update(2*node, l, mid, ql, qr, val)
        self.update(2*node+1, mid+1, r, ql, qr, val)
        
        if self.cover[node] > 0:
            self.len[node] = self.get_length(l, r)
        else:
            self.len[node] = self.len[2*node] + self.len[2*node+1]
    
    def update_range(self, ql, qr, val):
        """更新区间 [ql, qr]"""
        self.update(1, 0, self.n-1, ql, qr, val)
    
    def query(self):
        """查询被覆盖的总长度"""
        return self.len[1]


# Read first line safely
try:
    first_line = input().strip()
    while not first_line:  # Skip empty lines
        first_line = input().strip()
    n = int(first_line)
except EOFError:
    print(0)
    exit()

x_coords = []
y_coords = []
events = []

# 读取所有矩形
for _ in range(n):
    try:
        line = input().strip()
        while not line:  # Skip empty lines
            line = input().strip()
        x1, y1, x2, y2 = map(int, line.split())
    except EOFError:
        break
    
    x_coords.append(x1)
    x_coords.append(x2)
    y_coords.append(y1)
    y_coords.append(y2)
    
    events.append((y1, x1, x2, 1))   # 矩形开始
    events.append((y2, x1, x2, -1))  # 矩形结束

# 坐标离散化
x_coords = sorted(set(x_coords))
y_coords = sorted(set(y_coords))

# 建立坐标到索引的映射
x_map = {coord: i for i, coord in enumerate(x_coords)}
y_map = {coord: i for i, coord in enumerate(y_coords)}

# 将事件中的坐标转换为离散化后的索引
events_discrete = []
for y, x1, x2, event_type in events:
    events_discrete.append((y_map[y], x_map[x1], x_map[x2], event_type))

# 按 y 坐标排序事件
events_discrete.sort(key=lambda e: e[0])

# 扫描线算法
st = SegmentTree(x_coords)  # 传入实际坐标数组
total_area = 0

for i, (y, x1, x2, event_type) in enumerate(events_discrete):
    if i > 0 and y > events_discrete[i-1][0]:
        # 计算上一个 y 区间的面积
        covered_len = st.query()
        height = y_coords[y] - y_coords[events_discrete[i-1][0]]
        total_area += covered_len * height
    
    # 更新线段树：x2-1 因为线段树维护的是区间索引
    # 矩形 [x1, x2) 对应区间 [x1, x2-1]
    st.update_range(x1, x2 - 1, event_type)

print(total_area)

