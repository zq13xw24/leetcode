class Solution(object):
    def HammingDistance(self, x, y):
        a = bin(x).split('b')[1]
        b = bin(y).split('b')[1]
        if len(a) < len(b):
            a_2 = a.zfill(len(b))
            b_2 = b                     # 记得在每个if里面都要将所有的变量赋值
        else:
            b_2 = b.zfill(len(a))
            a_2 = a
        HD = 0
        for i in range(len(a_2)):
            if a_2[i] != b_2[i]:
                HD += 1
        return HD

a = Solution()
print(a.HammingDistance(2, 4))