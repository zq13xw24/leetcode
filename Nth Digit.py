'''
找出自然数序列的第n个数字是几
比如3——3， 11——0(10的第二位数字)
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1  # 位数
        while n > k * 9 * 10 ** (k - 1):
            n -= k * 9 * 10 ** (k - 1)
            k += 1
        if n % k == 0:
            t = n // k  # 第几个数字
        else:
            t = n // k + 1

        num = 10 ** (k - 1) + (t - 1)  # 目标数字
        temp = n - (t - 1) * k  # 目标数所在位数
        num_list = []
        while num > 0:  # 数字分解
            num_list.append(num % 10)
            num = num // 10
        return num_list[k - temp]  # 倒序取



    def findNthDigit2(self, n):
        if n < 0:
            return 0
        count = 9
        start = 1
        length = 1
        while n > (length * count):
            n -= length * count    # 去掉
            length += 1
            start *= 10
            count *= 10
        start += (n - 1) / length
        return int((str(start)[(n - 1) % length]))

# 大概懂了，如果n = 25，正确答案是7
# n > 9 但是 < 90 ，所以是在两位数里面。start变为10，那么这个数字就应该再10+.(n - 1) / 2 里面，也就是说在17里面的一个数，如果刚好除尽
# 就是第一个，除不尽就是第二个。欧力给