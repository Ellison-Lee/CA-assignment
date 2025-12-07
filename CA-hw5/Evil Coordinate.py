"""
Evil Coordinate - 机器人避雷问题

算法思路：
1. 统计各方向移动次数
2. 计算最终位置，如果是地雷位置则无解
3. 尝试不同的指令排列顺序（按方向分组），检查路径是否经过地雷
4. 使用贪心策略：先执行某个方向的所有指令，再执行其他方向

时间复杂度：O(n) - 只需要统计和模拟一次路径
空间复杂度：O(1) - 只需要常数额外空间
输出：5
1 1
RURULLD
0 5
UUU
0 3
UUU
0 2
UUU
0 0
UUU
输出：
LDLRUUR
UUU
Impossible
Impossible
Impossible

"""

def check_path_safe(moves, mx, my):
    """
    检查给定的移动序列是否安全（不经过地雷）
    
    Args:
        moves: 移动指令字符串
        mx, my: 地雷坐标
    
    Returns:
        bool: 如果路径安全返回True，否则返回False
    """
    x, y = 0, 0
    
    # 如果地雷在起点，第一步必须避开
    if mx == 0 and my == 0:
        return False
    
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        
        # 检查是否踩到地雷
        if x == mx and y == my:
            return False
    
    return True

def solve(mx, my, instructions):
    """
    解决机器人避雷问题
    
    Args:
        mx, my: 地雷坐标
        instructions: 原始指令字符串
    
    Returns:
        str: 重新排列的指令字符串，或 "Impossible"
    """
    # 特殊情况：如果没有指令
    if not instructions:
        if mx == 0 and my == 0:
            return "Impossible"
        return ""
    
    # 统计各方向的移动次数
    count_U = instructions.count('U')
    count_D = instructions.count('D')
    count_L = instructions.count('L')
    count_R = instructions.count('R')
    
    # 计算最终位置
    final_x = count_R - count_L
    final_y = count_U - count_D
    
    # 如果最终位置就是地雷，无解
    if final_x == mx and final_y == my:
        return "Impossible"
    
    # 如果地雷在原点，需要特殊处理
    if mx == 0 and my == 0:
        return "Impossible"
    
    # 构建基础指令字符串（按方向分组）
    moves_L = 'L' * count_L
    moves_R = 'R' * count_R
    moves_U = 'U' * count_U
    moves_D = 'D' * count_D
    
    # 尝试不同的排列顺序
    # 策略：尝试24种可能的方向排列（4! = 24）
    # 但实际上我们可以用更智能的方式
    
    # 尝试的顺序列表（常见的有效排列）
    orderings = [
        [moves_L, moves_R, moves_U, moves_D],
        [moves_L, moves_R, moves_D, moves_U],
        [moves_R, moves_L, moves_U, moves_D],
        [moves_R, moves_L, moves_D, moves_U],
        [moves_U, moves_D, moves_L, moves_R],
        [moves_U, moves_D, moves_R, moves_L],
        [moves_D, moves_U, moves_L, moves_R],
        [moves_D, moves_U, moves_R, moves_L],
        [moves_L, moves_U, moves_R, moves_D],
        [moves_L, moves_U, moves_D, moves_R],
        [moves_L, moves_D, moves_R, moves_U],
        [moves_L, moves_D, moves_U, moves_R],
        [moves_R, moves_U, moves_L, moves_D],
        [moves_R, moves_U, moves_D, moves_L],
        [moves_R, moves_D, moves_L, moves_U],
        [moves_R, moves_D, moves_U, moves_L],
        [moves_U, moves_L, moves_D, moves_R],
        [moves_U, moves_L, moves_R, moves_D],
        [moves_U, moves_R, moves_D, moves_L],
        [moves_U, moves_R, moves_L, moves_D],
        [moves_D, moves_L, moves_U, moves_R],
        [moves_D, moves_L, moves_R, moves_U],
        [moves_D, moves_R, moves_U, moves_L],
        [moves_D, moves_R, moves_L, moves_U],
    ]
    
    # 尝试每种排列
    for ordering in orderings:
        candidate = ''.join(ordering)
        if check_path_safe(candidate, mx, my):
            return candidate
    
    return "Impossible"

def main():
    """主函数：读取输入并输出结果"""
    try:
        # 读取第一行：测试用例数量
        first_line = input().strip()
        while not first_line:  # 跳过空行
            first_line = input().strip()
        T = int(first_line)
        
        # 处理每个测试用例
        for _ in range(T):
            # 读取地雷坐标
            mine_line = input().strip()
            while not mine_line:  # 跳过空行
                mine_line = input().strip()
            mx, my = map(int, mine_line.split())
            
            # 读取指令字符串
            instr_line = input().strip()
            while not instr_line:  # 跳过空行
                instr_line = input().strip()
            instructions = instr_line
            
            # 求解并输出结果
            result = solve(mx, my, instructions)
            print(result)
    
    except EOFError:
        exit()

if __name__ == "__main__":
    main()

