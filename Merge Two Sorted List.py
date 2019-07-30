"""
Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def mergeTwoList(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        dummy = ListNode(0)
        tmp = dummy      # 这个是表头哦
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next     # tmp要先跳到下一位才能继续往下一位添加啊。这么简单想什么呢
            else:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
        if l2 == None:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next