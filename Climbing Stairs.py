class Solution(object):
    def climbStairs(self, n):            # 发现就是斐波那契啊，斐波那契就是n1=1, n2=2, ni=n(i-2)+n(i-1)
        pre = cur = 1
        for i in range(n):
            pre, cur = cur, pre + cur
        return cur
