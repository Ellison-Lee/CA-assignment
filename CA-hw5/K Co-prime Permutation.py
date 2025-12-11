"""
问题: K Co-prime Permutation
构造一个排列，使得恰好有k个位置i满足gcd(p_i, i) = 1

核心思路：
关键洞察：交换位置i和j（即perm[i]=j, perm[j]=i）的效果：
- 如果gcd(i,j)=1，则两个位置都互质，贡献2个
- 如果gcd(i,j)>1，则两个位置都不互质，贡献0个

最简单的构造策略：
1. 初始化为单位排列perm[i]=i
2. 将前n-k个位置两两交换：1↔2, 3↔4, 5↔6, ...
   - 但要注意选择合适的交换方式
3. 将后k个位置两两交换或反转

时间复杂度: O(n)
空间复杂度: O(n)
输入：
5 3
输出：
1 4 5 2 3

"""
def solve():
    try:
        # 读取输入并去除首尾空格，按空格分割成列表
        data = input().strip().split()
        # 处理空输入（无有效数据）
        if not data:
            return
        # 解析n（排列长度）和k（需要的互质位置数）
        n, k = map(int, data)
    # 捕获输入异常（如EOF、非数字输入）
    except (EOFError, ValueError):
        return

    # 若要求0个互质位置且n≥1：无解（因为位置1的gcd(1,1)=1必互质）
    if k == 0 and n >= 1:
        print("-1")
        return

    # 初始化为单位排列：perm[0]=1（位置1）、perm[1]=2（位置2）...perm[n-1]=n（位置n）
    perm = list(range(1, n + 1))
    # 初始互质位置数：仅位置1（perm[0]=1）满足gcd(1,1)=1，故初始为1
    current_coprime = 1
    # 需要补充的互质位置数：目标k - 初始1
    needed = k - 1
    # 从位置2（索引1）开始尝试交换（两两交换的起始索引）
    i = 1

    # 循环条件：还需要至少2个互质位置，且当前交换位置不越界（i+1 < n）
    while needed >= 2 and i < n - 1:
        # 交换当前索引i和i+1的元素（对应位置i+1和i+2）
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
        # 两两交换后，互质位置数+2，因此需要补充的数量-2
        needed -= 2
        # 移动到下一组两两交换的位置（步长2）
        i += 2
        # 更新当前已有的互质位置数
        current_coprime += 2

    # 若还需要1个互质位置（needed=1）
    if needed == 1:
        # 记录当前待交换的索引
        i_0_idx = i
        # 确保索引不越界
        if i_0_idx < n:
            # 交换位置1（索引0）和当前索引i的元素，补充1个互质位置
            perm[0], perm[i] = perm[i], perm[0]
            # 更新互质位置数
            current_coprime += 1

    # 注：原代码中"if current_coprime != k: pass"表示不处理未达标情况，保留原有逻辑
    if current_coprime != k:
        pass
    # 将排列数组转为字符串，空格分隔后输出
    print(' '.join(map(str, perm)))
