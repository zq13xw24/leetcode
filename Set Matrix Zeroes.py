# 给定一个m x n的矩阵，如果元素出现了0，那么将整行或者整列变为0，中等难度
class Solution(object):
    def setZeros(self, matrix):
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]           # 弄一个状态，这里的i,j就可以代表行列了
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# 这题特别漂亮，先通过matrix[i][j]找到0的元素，并将该行和该列赋一个状态。再行列遍历一次，当发现那些状态时，令matrix[i][j] = 0


a = Solution()
print(a.setZeros([[1,1,1],[1,0,1],[1,1,1]]))