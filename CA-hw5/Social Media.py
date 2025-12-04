"""
社交媒体评论可见性问题

问题描述：
- 用户C要看到用户A在用户B帖子下的评论，必须同时是A和B的好友
- 如果用户在自己帖子下评论，所有他的朋友都能看到
- 目标：最多添加2个新朋友，使能看到的评论数最大化

算法思路：
1. 将所有评论按照可见性分类：
   - 当前已可见
   - 需要添加1个特定朋友才能看到
   - 需要添加2个特定朋友才能看到

2. 枚举所有可能的添加方案（0个、1个或2个新朋友）

3. 使用集合操作高效计算每种方案的收益

时间复杂度：O(m + C^2)
- m: 评论数
- C: 候选朋友数（出现在评论中但不是当前朋友的用户数）

空间复杂度：O(m + C)
"""


def count_visible_comments(friends, comments):
    """计算当前能看到的评论数"""
    friend_set = set(friends)
    count = 0
    
    for a, b in comments:
        if a == b:
            # 自己评论自己的帖子，只要是 a 的朋友就能看到
            if a in friend_set:
                count += 1
        else:
            # 评论别人的帖子，需要同时是 a 和 b 的朋友
            if a in friend_set and b in friend_set:
                count += 1
    
    return count


def solve(n, m, k, friends, comments):
    """
    解决社交媒体评论可见性问题
    
    参数：
    n: 当前朋友数
    m: 评论数
    k: 平台用户数
    friends: 当前朋友列表
    comments: 评论列表，每个元素是 (a, b) 表示用户a在用户b的帖子下评论
    
    返回：
    最多添加2个新朋友后能看到的最大评论数
    """
    friend_set = set(friends)
    
    # 分类评论：当前可见、需要1个新朋友、需要2个新朋友
    visible = 0  # 当前可见的评论数
    need_one = {}  # need_one[user] = 添加user作为朋友后能额外看到的评论索引集合
    need_two = {}  # need_two[(u1, u2)] = 需要同时添加u1和u2才能看到的评论索引集合
    
    for idx, (a, b) in enumerate(comments):
        if a == b:
            # 自己评论自己的帖子
            if a in friend_set:
                visible += 1
            else:
                # 需要添加a作为朋友
                if a not in need_one:
                    need_one[a] = []
                need_one[a].append(idx)
        else:
            # 评论别人的帖子
            a_is_friend = a in friend_set
            b_is_friend = b in friend_set
            
            if a_is_friend and b_is_friend:
                visible += 1
            elif a_is_friend and not b_is_friend:
                # 需要添加b
                if b not in need_one:
                    need_one[b] = []
                need_one[b].append(idx)
            elif not a_is_friend and b_is_friend:
                # 需要添加a
                if a not in need_one:
                    need_one[a] = []
                need_one[a].append(idx)
            else:
                # 需要同时添加a和b
                key = tuple(sorted([a, b]))
                if key not in need_two:
                    need_two[key] = []
                need_two[key].append(idx)
    
    max_count = visible
    
    # 情况1：添加1个新朋友
    for user, comment_indices in need_one.items():
        count = visible + len(comment_indices)
        max_count = max(max_count, count)
    
    # 情况2：添加2个新朋友
    candidates = list(need_one.keys())
    
    # 2.1: 添加两个都在need_one中的朋友
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            u1, u2 = candidates[i], candidates[j]
            # 计算添加u1和u2后能看到的评论
            seen_indices = set()
            seen_indices.update(need_one[u1])
            seen_indices.update(need_one[u2])
            
            # 检查need_two中是否有恰好需要这两个人的评论
            key = tuple(sorted([u1, u2]))
            if key in need_two:
                seen_indices.update(need_two[key])
            
            count = visible + len(seen_indices)
            max_count = max(max_count, count)
    
    # 2.2: 添加恰好need_two中的两个人
    for (u1, u2), comment_indices in need_two.items():
        seen_indices = set(comment_indices)
        
        # 同时检查这两个人在need_one中能带来的评论
        if u1 in need_one:
            seen_indices.update(need_one[u1])
        if u2 in need_one:
            seen_indices.update(need_one[u2])
        
        count = visible + len(seen_indices)
        max_count = max(max_count, count)
    
    return max_count


def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取测试用例数
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        T = int(first_line)
        
        for _ in range(T):
            # 读取 n, m, k
            line = input().strip()
            while not line:  # 跳过空行
                line = input().strip()
            n, m, k = map(int, line.split())
            
            # 读取朋友列表
            if n > 0:
                line = input().strip()
                while not line:  # 跳过空行
                    line = input().strip()
                friends = list(map(int, line.split()))
            else:
                friends = []
            
            # 读取评论列表
            comments = []
            for _ in range(m):
                line = input().strip()
                while not line:  # 跳过空行
                    line = input().strip()
                a, b = map(int, line.split())
                comments.append((a, b))
            
            # 求解并输出结果
            result = solve(n, m, k, friends, comments)
            print(result)
            
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

