class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                if (
                    curr in rows[r] or
                    curr in cols[c] or
                    curr in boxes[(r//3, c//3)]
                ):
                    return False
                
                rows[r].append(curr)
                cols[c].append(curr)
                boxes[(r//3, c//3)].append(curr)
        
        return True