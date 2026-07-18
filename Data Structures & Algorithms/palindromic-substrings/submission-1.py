class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(0, len(s)):
            # Explore and include all palindromes of odd length 1️⃣
            res += self.explore_palindromes(i, i, s)
            # Explore and include all palindromes of even length 2️⃣
            res += self.explore_palindromes(i, i+1, s)
        
        # All segments explored -> return their sum ✅
        return res

    def explore_palindromes(
        self,
        l: int,
        r: int,
        s: str
    ) -> int:
        current_palindrome_count = 0
        
        # For a string to count as a valid palindrome here, it has to be in the valid
        # range, and it has to satisfy the definition of the palindrome itself

        # We only check the first and last character, since we've already checked the inner
        # portion of this segment in a prior iteration

        # To minimize the code in the main function, we start from scratch, meaning we
        # check the innermost one or two elements here first
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # Condition satisfied; increase count! ✅
            current_palindrome_count += 1

            # Keep expanding 👈🏻👉🏻
            l -= 1
            r += 1
        
        # The entire segment explored; update the main variable with this return 👆🏻
        return current_palindrome_count