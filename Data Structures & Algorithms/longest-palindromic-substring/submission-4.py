class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        maxLen = 1

        for i in range(0, len(s)):
            res, maxLen = self.expand_palindrome(i-1, i+1, s, res, maxLen)
            res, maxLen = self.expand_palindrome(i, i+1, s, res, maxLen)
        
        return res
    
    def expand_palindrome(self, l: int, r: int, s: str, res: str, maxLen: int) -> tuple(str, int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > maxLen:
                res = s[l:r+1]
                maxLen = r-l+1
            l -= 1
            r += 1
        return res, maxLen