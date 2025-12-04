"""
问题3: 二叉树重建与后序遍历 (Binary Tree Reconstruction)
根据先序和中序遍历重建二叉树，然后输出后序遍历结果
时间复杂度: O(n^2) - 由于使用index查找

输入格式：
多行，每行包含两个字符串（先序遍历和中序遍历），用空格分隔
空行表示输入结束

输出格式：
对于每行输入，输出对应的后序遍历结果

示例：
输入：
ABDECF DBEAFC
输出：
DEBFCA
"""


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    """
    根据先序和中序遍历重建二叉树
    
    算法原理：
    - 先序遍历的第一个元素是根节点
    - 在中序遍历中找到根节点，左边是左子树，右边是右子树
    - 递归构建左右子树
    
    :param preorder: 先序遍历序列
    :param inorder: 中序遍历序列
    :return: 重建的二叉树根节点
    """
    if not preorder or not inorder:
        return None
    
    # 先序遍历的第一个字符是根节点
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # 在中序遍历中找到根节点的位置
    root_idx = inorder.index(root_val)
    
    # 递归构建左右子树
    root.left = build_tree(preorder[1:root_idx+1], inorder[:root_idx])
    root.right = build_tree(preorder[root_idx+1:], inorder[root_idx+1:])
    
    return root


def postorder_traversal(root):
    """
    后序遍历：左->右->根
    
    :param root: 二叉树根节点
    :return: 后序遍历结果字符串
    """
    if not root:
        return ""
    
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    
    return left + right + root.val


def main():
    """主函数：读取输入并输出结果"""
    try:
        while True:
            # 读取输入
            line = input().strip()
            if not line:  # 空行表示结束
                break
            
            parts = line.split()
            if len(parts) == 2:
                preorder, inorder = parts
                # 重建二叉树
                root = build_tree(preorder, inorder)
                # 后序遍历
                postorder = postorder_traversal(root)
                # 输出结果
                print(postorder)
                
    except EOFError:
        exit()


if __name__ == "__main__":
    main()

