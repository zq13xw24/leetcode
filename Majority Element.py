class Solution(object):
    def majorElement(self, nums):
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i) > len(nums) / 2:
                return i

    def majorElement2(self, nums):
        sort_nums = nums.sort()
        return sort_nums[len(nums)/2]

