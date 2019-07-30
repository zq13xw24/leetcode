'''
将二叉树转化为排序的双向链表，不能创建节点，只能调整指针的指向
'''

# 二叉树的中序排列就是一个非减的排列，先中序排列，再调整指针

class Solution:

    def inOrderTraverse(self, pRootOfTree):
        if not pRootOfTree:
            return []
        return self.inOrderTraverse(pRootOfTree.left) + [pRootOfTree] + self.inOrderTraverse(pRootOfTree.right)


    def Convert(self, pRootOfTree):
        res = self.inOrderTraverse(pRootOfTree)
        if len(res) == 0:
            return None
        if len(res) == 1:
            return pRootOfTree
        res[0].left = None
        res[0].right = res[1]
        res[-1].left = res[-2]
        res[-1].right = None
        for i in range(1, len(res)-1):
            res[i].left = res[i-1]
            res[i].right = res[i+1]
        return res[0]