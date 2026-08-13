class Solution(object):
    def markinfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float('-inf')

        for j in range(c):
            if matrix[row][j] != 0:
                matrix[row][j] = float('-inf')

    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markinfinity(matrix, i, j)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float('-inf'):
                    matrix[i][j] = 0

        return matrix


'''
TC=o((n+m)*(n*m)+(n*m))
SC=o(1)
'''

#optimal solution 
class Solution(object):

    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        row_track = [0] * r
        col_track = [0] * c

        # Track rows and columns containing 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1

        # Set corresponding rows and columns to 0
        for i in range(r):
            for j in range(c):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0

        return matrix

'''
TC=o(2(m*n))~ o(m*n)
SC=o(m+n)
'''