class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(0, len(s)):
            res += self.expand_palindrome(i, i, s)
            res += self.expand_palindrome(i, i+1, s)
        
        return res

    def expand_palindrome(
        self,
        l: int,
        r: int,
        s: str
    ) -> int:
        current_palindrome_count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current_palindrome_count += 1
            l -= 1
            r += 1
        return current_palindrome_count