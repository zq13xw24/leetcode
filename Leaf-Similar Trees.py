# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, res):
            if not root:
                return True
            else:
                if not root.left and not root.right:
                    res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
            return res
        res1 = dfs(root1, [])
        res2 = dfs(root2, [])
        return res1 == res2

# 像这种树好像一般都是这样遍历的。