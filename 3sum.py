"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""

# 可以利用2sum的思想

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -x-v, x))
        return map(list, res)

    def threeSum_2(self, nums):
        res = []
        for j in range(len(nums)):
            dict = {}         # 之前这里出现的错误的原因是将这个dict初始化放外面了，每次的target应该都需要一个新的dict才行
            target = nums[j]
            for i, v in enumerate(nums[j+1:]):
                if v in dict:
                    res.append(sorted([target, nums[dict[v]+j+1], nums[i+j+1]]))
                dict[-target - v] = i
        res = [list(t) for t in set(tuple(_) for _ in res)]
        return res
a = Solution()
print(a.threeSum_2([-1, 0, 1, 2, -1, -4]))


