class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m-1):
            newRow = [1] * n
            for i in range(n-2, -1, -1):
                newRow[i] = newRow[i+1] + row[i]
            row = newRow
        
        return row[0]