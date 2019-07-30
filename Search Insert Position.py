# Input: [1,3,5,6], 5
# Output: 2
# Input: [1,3,5,6], 2
# Output: 1
# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target <nums[i+1]:
                return i+1