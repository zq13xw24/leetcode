class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        reverse = []
        index = []
        keep = {}
        dreverse = {}
        ss = str()
        for i, v in enumerate(s):
            if v in vowels:
                reverse.append(v)
                index.append(i)
            else:
                keep[i] = v
        reverse = reverse[::-1]
        for i in range(len(index)):
            dreverse[index[i]] = reverse[i]
        ans = {**keep, **dreverse}
        ans = sorted(ans.items(), key=lambda item: item[0])
        for i in ans:
            ss = ss + str(i[1])
        return ss

a = Solution()
s = 'hello'
print(a.reverseVowels(s))

r = ['a', 'b', 'a', 'a']
m = 'b'
print()
