class Solution(object):
    def validParenthese(self, s):
        left = ['(', '[', '{']
        right = [')', ']', '}']
        length1 = []
        length2 = []
        stack = []
        if len(s) == 0:
            return True
        for j in s:
            if j in left:
                length1.append(j)
            elif j in right:
                length2.append(j)
        if len(length1) != len(length2):
            return False
        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                if len(stack) == 0:
                    return False
                if right.index(i) != left.index(stack.pop()):
                    return False
        else:
            return True            # 注意这里的True要在循环外面，因为循环里面是找错。如果在循环里面，匹配一次就True了
a = Solution()
print(a.validParenthese("[(({})}]"))