class Solution(object):
    def reverse(self, x):
        x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return x
