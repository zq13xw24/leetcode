'''
计算所有的left leaves的和
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        ans = 0
        while stack != []:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    ans += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans