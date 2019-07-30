'''
判断是不是平衡的二叉树，也就是说左右高度相差不超过1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def balance(root):
            if root is None:
                return 0
            left = balance(root.left)
            right = balance(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return balance(root) != -1


