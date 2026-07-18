class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, ocean, prev):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in ocean or
                prev > heights[r][c]
            ):
                return
            
            ocean.add((r, c))

            for dr, dc in directions:
                dfs(r+dr, c+dc, ocean, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS-1, atlantic, 0)
        
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS-1, c, atlantic, 0)
        
        return list(atlantic.intersection(pacific))