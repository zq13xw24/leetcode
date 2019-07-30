# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 对于任意节点node，它的左子树的所有后代节点都小于这一节点的值
# 对于任意节点node，它的右子树的所有后代节点的值都大于这一节点的值
class Solution(object):
#     def isValidBST(self, root):
#         if root[2] > root[0] > root[1] :
#             if len(root) < 4:
#                 return True
#             else:
#                 for i in range(3, len(root)):
#                     if root[i+1] > root[i-1] > root[i]:
#                         return True
#                     else:
#                         return False
#         else:
#             return False                      # 不能用索引，日了狗



    def isValidBST_2(self, root):
        return self.isValid(root, -2147483648.1, 2147483647.1)

    def isValid(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)
# 递归：棵树是二叉查找树，那么左子树的节点值一定处于（负无穷，root.val）这个范围内，右子树的节点值一定处于（root.val，正无穷）这个范围内。
# （注意边界值，负无穷和正无穷换成浮点型的极值）




# a = Solution()
# print(a.isValidBST([5,1,4,3,6]))
