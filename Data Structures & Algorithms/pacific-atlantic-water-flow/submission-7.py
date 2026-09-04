class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        lr, lc = ROWS-1, COLS-1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def bfs(q: deque, ocean: set) -> None:
            while q:
                r, c = q.popleft()

                ocean.add((r, c))

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    
                    if (
                        min(nr, nc) < 0 or
                        nr > lr or nc > lc or
                        (nr, nc) in ocean or
                        heights[nr][nc] < heights[r][c]
                    ):
                        continue
                    
                    q.append((nr, nc))
        
        for r in range(ROWS):
            bfs(deque([(r, 0)]), pacific)
            bfs(deque([(r, lc)]), atlantic)
        
        for c in range(COLS):
            bfs(deque([(0, c)]), pacific)
            bfs(deque([(lr, c)]), atlantic)
        
        return list(atlantic.intersection(pacific))