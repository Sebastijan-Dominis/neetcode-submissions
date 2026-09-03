class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        lr, lc = ROWS-1, COLS-1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, ocean: set) -> None:
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
                
                dfs(nr, nc, ocean,)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, lc, atlantic)
        
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(lr, c, atlantic)
        
        return list(atlantic.intersection(pacific))