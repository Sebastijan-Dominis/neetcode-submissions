class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        exploring = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in exploring or
                board[r][c] != word[i]
            ):
                return False
            
            if i+1 == len(word):
                return True

            exploring.add((r, c))

            for dr, dc in directions:
                if dfs(r+dr, c+dc, i+1):
                    return True
            
            exploring.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False