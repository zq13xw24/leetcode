class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        set1 = set(nums)
        set2 = set(list(range(1, n+1)))
        return list(set2 - set1)