'''
数出小于n的质数的个数
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

# 本来在找x以内的质数的时候，就是将它除[2, x ** 0.5] 之内的数，看能否被整除
# 但这里不能遍历所有的n，因为这样的话肯定是超时的。
# 采用厄拉多塞筛法
# 将倍数赋值为false
# 这个需要记住了
