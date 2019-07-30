# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]
        # max = nums[0]
        # min = nums[0]
        # sum = 0
        # x = 0
        # y = 0
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     if sum - max > 0:
        #         max = sum
        #         x = i
        #     if sum - min < 0:
        #         min = sum
        #         y = i
        # return max - min

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# 这个是真的牛批。只要nums[i-1]是一个正向序列，那么就把它和nums[i]相加并赋值给nums[i]，经过赋值的nums[i]都是可能的最大的sum。
# 最后是一个max，所以也不用担心nums[i+1]让nums[i]减小。
