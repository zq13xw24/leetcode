'''
算阶乘之后末尾有多少个0
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def cal(n):
            if n < 0:
                return False
            if n == 0:
                return 1
            return n * cal(n-1)
        ans = cal(n)
        count = 0
        while ans / 10 == ans // 10:
            count += 1
            ans = ans / 10
            # if ans / 10 != ans // 10:
            #     break
        return count
# 超时啦

    def trailingZeroes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n >= 5:
            n //= 5
            cnt += n
        return cnt

# 这个解法很巧妙，因为只有偶数×5才会出现10，那么就需要将阶乘进行重新因式分解，分解成5和2的乘积，2不需要考虑
# 这里只需要考虑可以分解出来的5的个数，个数就是n//5
# 比如20，只有5,10,15,20能分解出来5，所以有4个，但是25的话，5,10,15,20,25可以分解出来6个5