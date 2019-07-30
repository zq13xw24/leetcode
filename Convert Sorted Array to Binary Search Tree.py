'''
给定一个内部元素按照升序排列的数组，请将其转化成高度平衡的二叉搜索树。
高度平衡的二叉树就是子树高度不能超过1
注意二叉树的性质是永远有左＜根＜右
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root_index = int(len(nums)/2) + 1
        list_left = nums[:root_index]
        list_right = nums[root_index+1:]
        ans = TreeNode(None)
        tmp = ans
        tmp.val = nums[root_index]
        for i in range(len(list_left)):
            tmp.left = list_left[-(i+1)]
            tmp = tmp.left
        for i in range(len(list_right)):
            tmp.left = list_right[-(i+1)]
            tmp = tmp.right
        return ans
# 赋值还不行鸭

    def sortedArrayToBST_2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root_index = int(len(nums)/2)
        list_left = nums[:root_index]
        list_right = nums[root_index+1:]
        if len(nums) != 0:
            root = TreeNode(nums[root_index])
            root.left = self.sortedArrayToBST_2(list_left)
            root.right = self.sortedArrayToBST_2(list_right)
        else:
            root = None
        return root

# 直接给搜索二叉树进行left和right的赋值是不行的。但是每次直接生成一个TreeNode是可以的，所以可以采取迭代的方式