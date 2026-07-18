class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToZero, colsToZero = [], []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToZero.append(i)
                    colsToZero.append(j)
        
        for i in rowsToZero:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in colsToZero:
                matrix[i][j] = 0