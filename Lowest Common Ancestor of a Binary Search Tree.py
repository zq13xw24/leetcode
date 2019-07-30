'''
找两个node的最近公共祖先节点，注意一个节点可以是本身的公共节点
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

# 搜索二叉树有一个性质，那就是左边小于节点，右边大于节点
# 如果p,q都小于root的话，那么肯定在root左边，大于同理。除开这两种情况的话，那一定就是root自己了