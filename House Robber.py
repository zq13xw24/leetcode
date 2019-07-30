'''
求一个列表不相邻元素相加最大的和
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums[0], nums[-1])
        money = [0] * len(nums)
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(nums[i] + money[i - 2], money[i - 1])
        return money[len(nums) - 1]


# 当然你会发现，上面的代码使用的空间是冗余的，因为每次循环只会用到前两个数据。所以代码可以降低空间复杂度到O(1)。

    def rob_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

# 假设有n家，那么你要判断“偷第n家不偷第n-1家且前n-2家尽量多的偷”和“不偷第n家且前n-1家尽量多的偷”，
# 哪个得到的钱多偷哪个。
# last和now这两个变量是相差一个的。now被赋值为last+i，此时的last并没有被赋值为上一个now，也就是说i与last相差了一位
# max里面的last+i是偷第i个，和i-2之前的和相加，now就是不偷i，偷i-1和i-1家之前的。
# 大概能理解这个神奇的代码了，背就完事了
