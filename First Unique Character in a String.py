'''
找到字符串中第一个非重复的元素的index，没有则返回-1
'''


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=[0]*256
        for char in s:
            temp[ord(char)]+=1
        for i in range(len(s)):
            if temp[ord(s[i])]==1:
                return i
        return -1

# 将s通过循环转换为List然后再遍历查看count的方法超时了