# Given nums = [1,1,2]
# answer = [1,2]
# 不能申请新的空间来生成列表，只能在原列表里面进行in-place
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1

# 反正思路就是一个一个往后比。