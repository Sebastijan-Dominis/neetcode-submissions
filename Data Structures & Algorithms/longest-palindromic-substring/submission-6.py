class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        for i in range(len(s)):
            res, maxLen = self.expandPalindrome(i, i, s, res, maxLen)
            res, maxLen = self.expandPalindrome(i, i+1, s, res, maxLen)

        return res

    def expandPalindrome(
        self,
        l: int,
        r: int,
        s: str,
        res: str,
        maxLen: int
    ) -> tuple(str, int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > maxLen:
                res = s[l:r+1]
                maxLen = (r-l+1)
            l -= 1
            r += 1
        
        return res, maxLen