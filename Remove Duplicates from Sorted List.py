# Input: 1->1->2
# Output: 1->2
# Input: 1->1->2->3->3
# Output: 1->2->3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        root = head
        current = head.next
        prev = head
        while current:
            if prev.val == current.val:
                prev.next = current.next     # 直接就跳到next的next了。这个题目应该是不能新建ListNode的，只能在原来的上改
                current = current.next
            else:
                prev = current

        return root