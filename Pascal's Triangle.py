'''
杨辉三角
'''

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def pascal(prev):
            res = []
            for i in range(len(prev) - 1):
                res.append(prev[i] + prev[i + 1])
            return [1] + res + [1]
        result = [[1]]
        for _ in range(numRows - 1):
            result.append(pascal(result[-1]))
        return result if numRows else []

# 这个杨辉三角的思路是通过一个函数生成中间的数，然后该函数输出加上头尾的1的数列