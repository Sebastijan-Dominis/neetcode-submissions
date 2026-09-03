class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lr, lc = ROWS-1, COLS-1

        islands = 0
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([])

        def bfs() -> None:
            while q:
                r, c = q.popleft()

                visit.add((r, c))

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (
                        min(nr, nc) < 0 or
                        nr > lr or nc > lc or
                        (nr, nc) in visit or
                        grid[nr][nc] != '1'
                    ):
                        continue
                    
                    visit.add((nr, nc))
                    q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    q.append((r, c))
                    islands += 1
                    bfs()
        
        return islands