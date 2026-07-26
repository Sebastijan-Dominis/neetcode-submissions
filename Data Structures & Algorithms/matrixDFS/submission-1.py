class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lr, lc = ROWS-1, COLS-1
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if grid[0][0] == 1 or grid[lr][lc] == 1:
            return 0

        def dfs(grid: list[list[int]], r: int, c: int) -> int:
            if r == lr and c == lc:
                return 1
            
            visit.add((r, c))
            count = 0

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if (
                    min(nr, nc) < 0 or
                    nr > lr or nc > lc or
                    grid[nr][nc] == 1 or
                    (nr, nc) in visit
                ):
                    continue
                
                count += dfs(grid, nr, nc)
            
            visit.remove((r, c))

            return count
        
        return dfs(grid, 0, 0)