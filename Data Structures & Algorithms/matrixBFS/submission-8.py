class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lr, lc = ROWS-1, COLS-1

        if grid[0][0] == 1 or grid[lr][lc] == 1:
            return -1
        
        visit = set((0, 0))
        shortest = 0
        q = deque([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == lr and c == lc:
                    return shortest

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (
                        min(nr, nc) < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                    ):
                        continue
                    
                    visit.add((nr, nc))
                    q.append((nr, nc))

            shortest += 1
        
        return -1