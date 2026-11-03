class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))
        
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == -1
                    ):
                        continue
                    
                    visit.add((nr, nc))
                    grid[nr][nc] = dist
                    q.append((nr, nc))
            
            dist += 1