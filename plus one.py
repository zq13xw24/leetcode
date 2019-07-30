# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 列表代替整数


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        anslist = []
        interger = 0
        for i, v in enumerate(digits):
            interger += int(v * 10 ** (len(digits) - i -1))
        ans = interger + 1
        for num in str(ans):
            anslist.append(int(num))
        return anslist



