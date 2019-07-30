

'''
给定一个二叉树，求其最小深度。
最小深度指的是，从根节点到最近的叶子节点的最近路径的节点个数。
深度优先搜索（DFS），用递归求解。注意，一个节点的最小高度不一定是两个子树的最小高度中较小的，
当一个子树为空时，该节点的最小高度等于另一个子树的最小高度。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            if not root.left:
                return 1 + self.minDepth(root.right)
            elif not root.right:
                return 1 + self.minDepth(root.left)
            else:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# 这种加一来进行递归计数的方法一定要掌握的