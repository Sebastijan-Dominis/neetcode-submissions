class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToZero, colsToZero = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToZero.add(i)
                    colsToZero.add(j)

        for i in rowsToZero:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in colsToZero:
                matrix[i][j] = 0