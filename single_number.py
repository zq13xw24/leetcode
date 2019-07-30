class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:  # 如果数组长度为1，则输出该数字。其实我这里考虑多了，题目的意思应该是该数组长度大于等于3
            return nums[0]
        else:
            nums.sort()  # 排序
            # 以下两个if判断头尾两个数字是否为single number
            if (nums[0] != nums[1]):
                return nums[0]
            if (nums[len(nums) - 1] != nums[len(nums) - 2]):
                return nums[len(nums) - 1]
            else:
                for i in range(1, len(nums) - 1):
                    if (nums[i] != nums[i + 1] and nums[i] != nums[i - 1]):
                        return nums[i]
