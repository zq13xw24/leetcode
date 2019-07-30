'''
平衡二叉树的三种排列的递归和非递归实现
先序：根——左——右
中序：左——根——右
后序：左——右——根
'''



class solution():

    # 先序，递归和非递归
    def preOrderTraverse(self, node):
        if not node:
            return None
        print(node.val)
        self.preOrderTraverse(node.left)
        self.preOrderTraverse(node.right)

    def preOrderTraverse_2(self, node):
        stack = [node]
        while len(stack) > 0:
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    # 中序，递归和非递归
    def inOrderTraverse(self, node):
        if not node:
            return None
        self.inOrderTraverse(node.left)
        print(node.val)
        self.inOrderTraverse(node.right)

    def inOrderTraverse_2(self, node):
        stack = []
        pos = node
        while pos or len(stack)>0:
            if pos:
                stack.append(pos)
                pos = pos.left
            else:
                pos = stack.pop()
                print(pos.val)
                pos = pos.right

    # 后序，递归和非递归
    def postOrderTraverse(self, node):
        if not node:
            return None
        self.postOrderTraverse(node.left)
        self.postOrderTraverse(node.right)
        print(node.val)

    def postOrderTraverse_2(self, node):
        stack = [node]
        stack2 = []
        while len(stack) > 0:
            node = stack.pop()
            stack2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while len(stack2) > 0:
            print(stack2.pop().val)

    