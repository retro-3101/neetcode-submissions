class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n, m = len(matrix), len(matrix[0])

        rowzero, colzero = False, False

        for num in matrix[0]:
            if num == 0:
                rowzero = True
        
        for i in range(n):
            if matrix[i][0] == 0:
                colzero = True
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if colzero:
            for i in range(n):
                matrix[i][0] = 0

        if rowzero:
            matrix[0] = [0]*m
        
        return