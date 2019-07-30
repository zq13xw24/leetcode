# 将一个二叉树反向输出
# [3,9,20,null,null,15,7]
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def levelOrderBottom(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if root is None: return []
    #     levels = [[root]]
    #     results = []
    #
    #     while levels:
    #         level = levels.pop()
    #
    #         result_row = [node.val for node in level]
    #         results.insert(0, result_row)
    #
    #         next_level = []
    #         for node in level:
    #             if node.left:
    #                 next_level.append(node.left)
    #             if node.right:
    #                 next_level.append(node.right)
    #
    #         if len(next_level) > 0:
    #             levels.append(next_level)
    #
    #     return results

    def levelOrderBottom_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, final = {}, []

        def bfs(root, d):
            if not root: return
            if d in ans:         # 如果该层已经出现了
                ans[d] += (root.val,)
            else:
                ans[d] = (root.val,)
            if root.left:
                bfs(root.left, d + 1)
            if root.right:
                bfs(root.right, d + 1)

        bfs(root, 0)
        for i in list(ans.keys())[::-1]:
            final.append(list(ans[i]))
        return final

# 非常好，看懂啦。冲鸭