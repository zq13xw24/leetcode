'''
判断列表中重复的数字之间的间隔是否小于等于k
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numIndex = {}
        for i, v in enumerate(nums):
            if v not in numIndex:
                numIndex[v] = i
            else:
                if i - numIndex[v] > k:
                    return False
                else:
                    numIndex[v] = i
        return True