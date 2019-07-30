# Input: ["flower","flow","flight"]
# Output: "fl"
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest_len = min([len(i) for i in strs])

        for i in range(shortest_len, -1, -1):       # shortest_len到0的倒序
            if len(set([j[:i] for j in strs])) == 1:            # set会去重的
                return strs[0][:i]
        return ""