class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return
            
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    visited_old = len(visited)
                    dfs(row, col)
                    visited_new = len(visited)
                    diff = visited_new - visited_old
                    max_area = max(max_area, diff)
        
        return max_area