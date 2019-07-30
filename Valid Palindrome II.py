# 任意删一个字符看是不是回文
class Solution(object):
    def validPalindrome(self, s):
        cleanlist = [c for c in s.lower() if c.isalnum()]
        for i in range(len(cleanlist)):
            cleanlist_silce = cleanlist[:i] + cleanlist[i+1:]           # 之所以是range(len(cleanlist))，是因为在切片的时候哦，
            if cleanlist_silce == cleanlist_silce[::-1]:
                return True
        return False                            # 超时了哎，对比第三个方法，我觉得应该是多了一个建立一个clean_list的过程吧

    def validPalindrome_2(self, s):
        l = len(s)
        if l == 2:
            return True
        i = 0
        j = l - 1
        count = 0
        while (i < j):
            if s[i] != s[j]:
                i += 1
                count += 1
            else:
                j -= 1
                i += 1
        if count < 2:
            return True
        count = 0
        i = 0
        j = l - 1
        while (i < j):
            if s[i] != s[j]:
                j -= 1
                count += 1
            else:
                j -= 1
                i += 1
        if count < 2:
            return True
        return False

    def validPalindrome_3(self, s):
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        size = len(s)
        lo, hi = 0, size - 1
        while lo < hi:
            if s[lo] != s[hi]:             # 碰到了不相等的，肯定是要删除的才行
                return isPalindrome(strPart(s, lo)) or isPalindrome(strPart(s, hi))
            lo += 1
            hi -= 1
        return True             # 好，先找到不同的，而且是从两端开始找的。找到了只需要执行一次if语句判断，而不需要每次都执行。




a = Solution()
print(a.validPalindrome('eccer'))