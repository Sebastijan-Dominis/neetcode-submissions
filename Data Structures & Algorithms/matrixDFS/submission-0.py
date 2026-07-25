class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()

        def helper(grid: list[list[int]], r: int, c: int) -> int:
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                grid[r][c] == 1
            ):
                return 0
            
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            visit.add((r, c))

            count = 0
            for dr, dc in directions:
                count += helper(grid, r+dr, c+dc)
            
            visit.remove((r, c))

            return count
        
        return helper(grid, 0, 0)