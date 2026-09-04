class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lr, lc = ROWS-1, COLS-1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        def dfs(r: int, c: int) -> None:
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if (
                    min(nr, nc) < 0 or
                    nr > lr or nc > lc or
                    (nr, nc) in visit or
                    grid[nr][nc] != '1'
                ):
                    continue
                
                dfs(nr, nc)
        
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        
        return islands