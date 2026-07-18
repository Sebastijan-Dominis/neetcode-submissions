class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        maxLen = 1

        for i in range(0, len(s)-1):
            currLen, currStr = self.expand_palindrome(i-1, i+1, s, 1, s[i])
            if currLen > maxLen:
                maxLen = currLen
                res = currStr

            if s[i] == s[i+1]:
                currLen, currStr = self.expand_palindrome(i-1, i+2, s, 2, s[i:i+2])
                if currLen > maxLen:
                    maxLen = currLen
                    res = currStr
        
        return res
    
    def expand_palindrome(self, l: int, r: int, s: str, startLen: int, startStr: str) -> tuple(int, str):        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            startLen += 2
            startStr = s[l] + startStr + s[r]
            l -= 1
            r +=1
        
        return startLen, startStr