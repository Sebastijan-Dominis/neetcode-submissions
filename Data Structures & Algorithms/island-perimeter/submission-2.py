class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        def dfs(r: int, c: int) -> None:
            nonlocal perimeter
            if (r, c) in visit:
                return

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                perimeter += 1
                return

            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return perimeter