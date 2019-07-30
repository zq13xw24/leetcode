# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# 回文对称  A man, a plan, a canal: Panama

class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        else:
            set = []
            for i in range(len(s)):
                if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z' or s[i] >= '0' and s[i] <= '9':
                    set.append(s[i].lower())
            for i in range(int(len(set) / 2)):
                if set[i] != set[len(set)-i-1]:
                    return False
            return True

    def isPalindrome_2(self, s):
        cleanlist = [c for c in s.lower() if c.isalnum()]           # isalnum() 方法检测字符串是否由字母和数字组成。
        return cleanlist == cleanlist[::-1]
