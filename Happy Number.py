'''
看一个数不停地拆分为各个数字的平方和最后是否为1
'''

class Solution(object):
    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

# 在那个集合中出现过了就肯定不能成功了
# 我自己写的时候想到用while来不停调用一个函数，但是没想到怎样作为停止while的条件，因为有可能一直循环没有解