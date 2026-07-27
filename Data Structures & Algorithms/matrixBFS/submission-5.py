class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lr, lc = ROWS-1, COLS-1
        
        if grid[0][0] == 1 or grid[lr][lc] == 1:
            return -1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set((0, 0))
        
        q = deque([(0, 0)])

        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == lr and c == lc:
                    return length
                
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    
                    if (
                        min(nr, nc) < 0 or
                        nr > lr or nc > lc or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                    ):
                        continue
                    
                    visit.add((nr, nc))
                    q.append((nr, nc))
            
            length += 1
        
        return -1