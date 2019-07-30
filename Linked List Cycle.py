'''
找链表中是否存在环
链表中的环就是一个环的结构，指向前面的一个元素
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next == None:
            return False
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 这个是这个题的经典解法，用快慢指针，如果没有环，那么快指针就会先碰到None，如果存在环的话，那么快慢指针总会碰到的