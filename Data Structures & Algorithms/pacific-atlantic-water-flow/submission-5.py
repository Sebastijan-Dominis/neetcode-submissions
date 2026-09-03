class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        lr, lc = ROWS-1, COLS-1
        atlantic, pacific = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(ocean: set, q: deque) -> None:
            while q:
                for _ in range(len(q)):
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
            bfs(pacific, deque([(r, 0)]))
            bfs(atlantic, deque([(r, lc)]))
        
        for c in range(COLS):
            bfs(pacific, deque([(0, c)]))
            bfs(atlantic, deque([(lr, c)]))
        
        return list(atlantic.intersection(pacific))