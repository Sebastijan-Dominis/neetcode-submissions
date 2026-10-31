class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0

        while row < len(matrix):
            l, r = 0, len(matrix[row]) - 1
            
            while l <= r:
            
                k = (l+r) // 2
                curr = matrix[row][k]

                if curr == target:
                    return True
                
                if curr < target:
                    l = k + 1
                else:
                    r = k - 1
            
            row += 1
        
        return False