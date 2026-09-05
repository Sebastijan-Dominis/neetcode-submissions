class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            total += self.explorePalindromes(i, i, s)
            total += self.explorePalindromes(i, i+1, s)
        
        return total

    def explorePalindromes(self, l: int, r: int, s: str) -> int:
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count