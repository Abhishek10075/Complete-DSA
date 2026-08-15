#optimal Solution ->Rotate in place
class Solution(object):
    def rotate(self, matrix):
        r=len(matrix)
        n=r
        c=len(matrix[0])
        result=[[0 for _ in range(r)]  for _ in range(r)]
        for i in range(0,r):
            for j in range(i+1,c):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,r):
            matrix[i].reverse()

'''
TC=o(n*m)+o(n*m)
SC=o(1)
'''