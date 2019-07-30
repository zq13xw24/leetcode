'''
矩阵顺时针输出
'''

class solution():

    def printMatrix(self, Matrix):
        result = []
        while(Matrix):
            result += Matrix.pop(0)
            if not Matrix:
                break
            Matrix = self.turn(Matrix)
        return result

    def turn(self, Matrix):
        newMatrix = []
        r = len(Matrix)
        c = len(Matrix[0])
        for i in range(c):
            _newMatrix = []
            for j in range(r):
                _newMatrix.append(Matrix[j][i])
            newMatrix.append(_newMatrix)
        newMatrix.reverse()
        return newMatrix


a = solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(a.printMatrix(matrix))
print(a.turn([[1,2,3],[4,5,6],[7,8,9]]))

# b = solution()
# print(b.turn([[1,2,3],[4,5,6]]))

# c = [[1,2,3],[4,5,6]]
# # print(len(c[0]))
# for i in range(len(c)):
#     for j in range(len(c[0])):
#         print(c[j][i])
