class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        word = str.split(' ')
        value = []
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != word[i]:
                    return False
            dic[pattern[i]] = word[i]
            value.append(word[i])      # 加这个是为了防止出现  abba  dog dog dog dog 
            if len(set(value)) != len(dic):
                return False
        return True

