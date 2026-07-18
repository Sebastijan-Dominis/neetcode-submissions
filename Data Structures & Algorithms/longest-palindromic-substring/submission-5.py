class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        for i in range(0, len(s)):
            # Check for odd palindromes 1️⃣
            res, maxLen = self.expand_palindrome(i, i, s, res, maxLen)
            # Check for even palindromes 2️⃣
            res, maxLen = self.expand_palindrome(i, i+1, s, res, maxLen)
        
        # Return the actual string 💬
        return res
    
    def expand_palindrome(
        self, 
        l: int, 
        r: int, 
        s: str, 
        res: str, 
        maxLen: int
    ) -> tuple(str, int):
        # Only continue while we're in the allowed range and the condition for a palindrome is satisfied 🛂
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # If we've reached the new longest palindrome, update result (res) and its length (maxLen)
            if (r-l+1) > maxLen:
                res = s[l:r+1]
                maxLen = r-l+1
            # Keep expanding, one by one
            l -= 1
            r += 1
        # Either we return the same as input (nothing changed) or new values (new longest palindrome found)
        return res, maxLen