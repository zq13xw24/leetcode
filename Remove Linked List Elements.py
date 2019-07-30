'''
移除链表中等于val的值
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            if curr.val == val:
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head

# 为什么是返回head呢？是在哪里对head进行了更改呢

    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while tmp.next:
            if tmp.next.val == val:      # 注意这里是tmp.next.val
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return dummy.next

# 这个就好理解多了