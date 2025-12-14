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
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder,inorder):
    if not preorder or not inorder: #递归结束条件
        return None

    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0]) #树元素有唯一性，可以直接通过值找到根节点在inorder的位置

    root.left = build_tree(preorder[1:idx+1],inorder[:idx]) #递归建立左子树
    root.right = build_tree(preorder[idx+1:],inorder[idx+1:]) #递归建立右子树

    return root

def postorder_query(root):
    if root is None: #递归遍历结束标志
        return ""
    
    left = postorder_query(root.left)
    right = postorder_query(root.right)

    return left+right+root.val


try:
    while True:
        line = input()
        if not line: break
        preorder,inorder = list(line.split())
        root = build_tree(preorder,inorder)
        print(postorder_query(root))
except EOFError:
    exit()