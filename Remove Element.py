class Solution(object):
    def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] == val:
                del nums[i]
        length = len(nums)
        return length            # 像这样倒着出现的索引为什么能克服在删除中不断变化的len导致的索引的对应问题呢


    def removeElement_2(self, nums, val):
        lastindex = len(nums) -1
        while 0 <= lastindex:
            if nums[lastindex] == val:
                del nums[lastindex]
            lastindex -= 1
        return len(nums)
# a = Solution()
# print(a.removeElement([0,4,4,0,4,4,4,0,2],4))
