class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] != '1'
            ):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands