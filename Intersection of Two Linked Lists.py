'''
找两个链表的交叉部分
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA and headB:
            return None
        tmp1 = headA
        tmp2 = headB
        while tmp1 != tmp2:
            tmp1 = headB if not tmp1 else tmp1.next
            tmp2 = headA if not tmp2 else tmp2.next
        return tmp1

# 用两个指针，1从第一个链表开始遍历，然后遍历第二个，2从第二个开始遍历然后遍历第一个
# 如果存在交叉点，那么两个指针就一定会同时便利到交集部分。和找环的思路有点像的呢！！！

print(ord('A'))


def cal(n):
    if n < 0:
        return False
    if n == 0:
        return 1
    return n * cal(n - 1)
print(120//10,125//10,125/10)