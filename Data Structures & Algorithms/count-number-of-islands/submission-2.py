class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lr, lc = ROWS-1, COLS-1

        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        def dfs(r: int, c: int) -> None:
            if (
                min(r, c) < 0 or
                r > lr or c > lc or
                (r, c) in visit or
                grid[r][c] != '1'
            ):
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr, nc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        
        return islands