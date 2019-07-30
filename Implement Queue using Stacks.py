'''
使用栈实现一个队列
'''


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.outStack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())  # 这里是在while循环里哦，是将所有的都append了
        return self.outStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.inStack and not self.outStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()