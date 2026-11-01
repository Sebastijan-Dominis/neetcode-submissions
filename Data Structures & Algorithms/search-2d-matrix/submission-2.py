class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        row = (top + bot) // 2

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if top > bot:
            return False
        
        l, r = 0, COLS-1

        while l <= r:
            m = (l+r) // 2
            curr = matrix[row][m]

            if target == curr:
                return True
            
            if target > curr:
                l = m + 1
            else:
                r = m - 1
        
        return False