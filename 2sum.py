class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        dict = {}
        for i, v in enumerate(nums):          # i是索引，v是值
            if v in dict:
                return [dict[v], i]
            dict[target - v] = i         # dict[]里面的东西是value
a = Solution()
print(a.twoSum([-1, 0, 1, 2, -1, -4], 0))

# 这个思想特别重要。不能循环两次啊。会time limited
# 理解，那个dict的作用呢，就是做一个映射，将nums每个索引i处的值差target多少做一个字典，差多少是dict的索引，i是dict的值。
# 因为要相加等于target，所以，与i对应的数字加起来为target的数字一定要是dict的索引
# 然后就返回差几的那个索引和几的索引

