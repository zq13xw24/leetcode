'''
判断两个字符串是否有相似的结构
例如 egg foo, add bcc
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        n = len(s)
        for i in range(n):
            if s[i] in char_map:
                if char_map[s[i]] != t[i]:
                    return False
            elif t[i] in char_map.values():  # 先出现了，这里的if和elif换一下也是可以的。
                return False
            else:
                char_map[s[i]] = t[i]
        return True

# 很巧妙，利用if 和 elif的非此即彼。在进行填入之后，一旦出现s[i]，但是字典里面对应的value不等于t[i]，那就错了
# 一旦出现t[i]，但是没有出现s[i]，也会出现错误，这里就是利用的if和elif
