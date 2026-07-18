class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        len_r = len(image)
        len_c = len(image[0])

        def dfs(r, c):
            if r < 0 or r >= len_r or c < 0 or c >= len_c or image[r][c] != orig:
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)

        return image