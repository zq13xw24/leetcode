class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
            if num / 2 == num // 2:
                num /= 2
            elif num / 3 == num // 3:
                num /= 3
            elif num / 5 == num // 5:
                num /= 5
            else:
                return False
        return True

dic = {}
index = [1,2,3,4,5]
val = [4,5,6,7,8]
dic[index] = val
print(dic)
