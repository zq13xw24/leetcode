class Solution(object):
    def moveZeros(self, nums):
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        # return nums               # 这个方法连续有两个0的情况就会出错
        for i in range(nums.count(0)):
            nums.remove(0)          # remove只能删除遇到的第一个0
            nums.append(0*nums.count(0))