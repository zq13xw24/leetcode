'''
反转一个链表
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

# 是真的牛批
# 注意这里不是返回的curr，而是返回的prev哦，prev记录了改变后的curr，而curr被破坏了，可以怎么理解
# 背就完事了